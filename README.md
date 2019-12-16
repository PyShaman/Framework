# Framework

Things to remember before running this framework:

1) You need to have installed one version of Python (3.6+). If you are
 using linux, remember to use pip3 when installing requirements (pip install -r requirements.txt).
 
2) You need to have Python added to your system path.

3) You need to have installed Java (at least 8) to run OWASP ZAP Proxy.
You need to have Java added to your system path.

4) You need to have installed git on your computer.

5) You need to have updated Chrome browser.

6) After you clone this repository to your disc, then copy your own
"credentials.json" and "token.json" to Framework/api/gmail directory.

7) Remember to change the email address to yours on the test_a (line 42)
in "test_01.py" file.

8) Remember to set proper interpreter to your PyCharm (it should be
the path to Python 3.6+ executable file and it should looks similar to
C:\Users\xxx\AppData\Local\Programs\Python\Python3X-YY\python.exe). If you see
few options to choose, you did something weird before, so to not waste
your time, reinstall PyCharm ;)

9) Remember to change proper port in zap.py (lines 12 and 14), 
test_01.py (line 24) files.

10) Remember to change proper path to OWASP ZAP Proxy executable in 
Framework/api/zap/zap.py file (line 23 and 24).

11) Have fun!
