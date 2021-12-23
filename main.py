import os
import schedule
import time

def job(self, loop):
    os.system("python proxyScraper.py -p http")
    time.sleep(60)
    os.system("python proxyChecker.py -s findanyanswer.com -l output.txt")
    time.sleep(120)
    os.system("python format.py")

schedule.every().hour.at(":00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)