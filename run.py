import subprocess
import schedule
import time

program_list = ['proxyScraper.py', 'proxyChecker.py', 'format.py']
param1 = ["-p", "http"]
param2 = ['-s', 'findanyanswer.com']
param3 = ['-l', 'output.txt']

def job():
    for program in program_list:
        if program is program_list[0]:
            subprocess.call(['python', program] + param1, shell=False)
            print("Finished:" + program)
        elif program is program_list[1]:
            subprocess.call(['python', program] + param2 + param3, shell=False)
            print("Finished:" + program)
        else:
            subprocess.call(['python', program], shell=False)
            print("Finished:" + program)

schedule.every(5).minutes.at(":00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)