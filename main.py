import requests
import sys
import os

cmd = input()
if cmd.find("epm install") != -1:
    package = cmd.split("epm install ")[1]
    rd = requests.get("https://raw.githubusercontent.com/ThatError404/EPM/main/Packages/" + package + "/required")
    if rd.status_code == 404:
        print("\nError: Package not found.")
        os.system(sys.executable + " main.py")
    elif rd.status_code == 200:
        print("\nPackage found. Installing...")
        required = rd.text.split("\n")
        r = requests.get("https://raw.githubusercontent.com/ThatError404/EPM/main/Packages/" + package + required[0])
        if not required[0] == "" or not required[0] == "\n":
            print("\n\nInstalling " + required[0])
            print("Collecting " + required[0])
            os.system("mkdir " + package)
            os.system("touch " + package + "/" + required[0])
            with open(package + "/" + required[0], "w") as f:
                f.write(requests.get("https://raw.githubusercontent.com/ThatError404/EPM/main/Packages/" + package + "/" + required[0]).text)
            size = os.path.getsize(package + "/" + required[0])
            print(" Downloading " + required[0] + " " + str(size) + " bytes")
            print(" Packing " + required[0])
            print(" " + required[0] + " packed.")
            print(required[0] + " installed.\n")
            os.system(sys.executable + " main.py")

elif cmd.find("epm uninstall") != -1:
    package = cmd.split("epm uninstall ")[1]
    print("\nUninstalling " + package)
    os.system("rm -rf " + package)
    print("\n" + package + " uninstalled.\n")
    os.system(sys.executable + " main.py")            

elif cmd == "exit":
    sys.exit()