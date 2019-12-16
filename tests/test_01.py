import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import api.gmail.gmail as mail
from selenium import webdriver
from selene.api import *
from webdriver_manager.chrome import ChromeDriverManager
from elements.pages.forgot_password import ForgotPassword
from elements.pages.email_sent import EmailSent
from api.zap.zap import Zap


class Test(unittest.TestCase):
    zap = Zap()
    zap.start_zap()
    zap.check_zap_connection()
    print("Zap initialized")

    @classmethod
    def setUpClass(cls):
        proxy_host = "127.0.0.1"
        proxy_port = "8095"
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--allow-running-insecure-content")
        options.add_argument(f"--proxy-server={proxy_host}:{proxy_port}")
        browser.set_driver(webdriver.Chrome(executable_path=ChromeDriverManager().install(), chrome_options=options))

    @classmethod
    def tearDownClass(cls):
        zap = Zap()
        zap.stop_zap()
        browser.quit_driver()

    @staticmethod
    def test_a():
        browser.open_url("https://the-internet.herokuapp.com/forgot_password")
        forgot_page = ForgotPassword()
        email_sent_page = EmailSent()
        forgot_page.input_email("your@email_here.com")
        forgot_page.click_button()
        email_sent_page.email_confirmation.should(have.text("Your e-mail's been sent!"))

    @staticmethod
    def test_b():
        gmail = mail.MailListener()
        print(gmail.get_mail_text())
        gmail.mark_message_as_read()

    @staticmethod
    def test_c():
        zap = Zap()
        zap.run_spider("https://the-internet.herokuapp.com/forgot_password")


if __name__ == '__main__':
    unittest.main(warnings='ignore')
