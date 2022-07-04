import requests
import time
import sys
import os

path = "C:/Program Files/"

user = os.getlogin()

if not os.path.exists("C:/Program Files/EPM"):
    os.mkdir(path + "EPM")
    os.system("echo > C:\Program Files\EPM\main.py")
    with open("C:\Program Files\EPM\main.py", "w") as f:
        f.write(requests.get("https://raw.githubusercontent.com/ThatError404/EPM/main/main.py").text)
    os.system("echo > C:/Users/" + user + "/epm.bat")
    with open("C:/Users/" + user + "/epm.bat", "w") as f:
        f.write(requests.get("https://raw.githubusercontent.com/ThatError404/EPM/main/epm.batch").text)
    print("\nChecking for errors...")
    if not os.path.exists("C:\Program Files\EPM"):
        print("\nError: Could not create C:\Program Files\EPM. Pleasew try to reinstall EPM or contact the developer.")
    else:
        print("\nEPM successfuly installed.\n")
    exit()
elif os.path.exists("C:/Program Files/EPM"):
    print("\nEPM is already installed.")
    exit()