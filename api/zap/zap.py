import time
import requests
import os
from retrying import retry
from subprocess import Popen, DEVNULL
import zapv2
from datetime import datetime


class Zap:
    def __init__(self):
        self.localProxy = {"http": "http://127.0.0.1:8096", "https": "http://127.0.0.1:8096"}
        self.host = "http://127.0.0.1"
        self.port = "8096"
        self.apikey = "al75sdd15vubce6vtahhkcscjn"
        self.zap = zapv2.ZAPv2(proxies=self.localProxy, apikey=self.apikey)
        self.core = self.zap.core
        self.spider = self.zap.spider

    @staticmethod
    def start_zap():
        print("Starting ZAP Proxy")
        process = Popen([r"C:\Program Files\OWASP\Zed Attack Proxy\zap.bat", "-silent"],
                        cwd=r"C:\Program Files\OWASP\Zed Attack Proxy",
                        stdin=None, stdout=DEVNULL, stderr=None, shell=True)
        time.sleep(1)
        print("ZAP process id: " + str(process.pid))

    def stop_zap(self):
        print("Shutdown ZAP")
        self.core.shutdown(apikey=self.apikey)

    @retry(stop_max_delay=40000)
    def check_zap_connection(self):
        return requests.get(f"{self.host}:{self.port}/").status_code

    def start_passive_scan(self):
        print("Starting passive scan")
        self.zap.pscan.set_enabled(enabled=True, apikey=self.apikey)

    def run_spider(self, target):
        print("Starting Scans on target: " + target)
        spider_scan_id = self.spider.scan(url=target, maxchildren=None, recurse=True, contextname=None,
                                          subtreeonly=None)
        print("Scan ID: " + spider_scan_id)
        # Give the Spider a chance to start
        time.sleep(2)
        while int(self.spider.status(spider_scan_id)) < 100:
            print("Spider progress " + self.spider.status(spider_scan_id) + "%")
            time.sleep(5)
        print("Spider scan completed")
        time.sleep(5)
        print("Saving HTML report to file")
        timestamp = str(datetime.now().isoformat()).replace(":", "-")[:-7]
        os.chdir(r"../../reports")
        my_file = open(f"ZAP_scan_{timestamp}.html", "w")
        my_file.write(self.core.htmlreport(self.apikey))
        my_file.close()
