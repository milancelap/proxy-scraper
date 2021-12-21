import os
import schedule
import time

def job():
    os.system("python proxyScraper.py -p http")
    time.sleep(60)
    os.system("python proxyChecker.py -s findanyanswer.com -l output.txt")
    time.sleep(120)
    os.system("python format.py")

schedule.every(60).minutes.at(":00").do(job)