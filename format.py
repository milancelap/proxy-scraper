from fileinput import FileInput
from os import write

w = open("proxies.txt", "w")

with FileInput(files=['output.txt'], inplace=False) as f:
    for line in f:
        line = line.rstrip()
        line = "\'http://"+line+"\'," 
        w.write(line+"\n")