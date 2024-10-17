import sys
import os
import requests
import subprocess
#denial of service
import time
system = sys.platform
#create background process for this so it doesn't flood the console
def background():
    with open("../background.log", "w") as log_file:
        process = subprocess.Popen(
            ["python", "weakdos.py"],
            stdout=log_file,
            stderr=subprocess.STDOUT
        )
    return process



background_process = background()
def background1():
    with open("../background.log", "w") as log_file:
        process = subprocess.Popen(
            ["python", "middos.py"],
            stdout=log_file,
            stderr=subprocess.STDOUT
        )
    return process

background_process1 = background1()

def background2():
    with open("../background.log", "w") as log_file:
        process = subprocess.Popen(
            ["python", "okdos.py"],
            stdout=log_file,
            stderr=subprocess.STDOUT
        )
    return process
background_process2 = background2()
def background3():
    with open("../background.log", "w") as log_file:
        process = subprocess.Popen(
            ["python", "eh.py"],
            stdout=log_file,
            stderr=subprocess.STDOUT
        )
    return process
background_process3 = background3()



