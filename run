#!/bin/bash
import subprocess

program_list = ['python proxyScraper.py -p http', 'python proxyChecker.py -s findanyanswer.com -l output.txt', 'python format.py']

for program in program_list:
    subprocess.call(['python', program])
    print("Finished:" + program)