import os
import schedule
import time

def job():
    os.system("python proxyScraper.py -p http")
    time.sleep(60)
    os.system("python proxyChecker.py -s findanyanswer.com -l output.txt")

schedule.every(60).minutes.at(":00").do(job)