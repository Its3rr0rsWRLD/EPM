import requests
import sys
import os

os.system("cls")
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
    if package == "epm":
        print("\nUninstalling EPM...")
        os.system("rmdir /S /Q C:\Program Files\EPM")
    else:
        print("\nUninstalling " + package)
        os.system("rmdir /S /Q " + package)
        print("\n" + package + " uninstalled.\n")
        os.system(sys.executable + " main.py")     

elif cmd.find("epm search") != -1:
    package = cmd.split("epm search ")[1]
    if package == "epm":
        answer = input("\nAre you sure you want to uninstall EPM? (y/n) ")
        if answer == "y":
            os.system("rmdir /S /Q EPM")
        elif answer == "n":
            os.system(sys.executable + " main.py")
    print("\nSearching for " + package)
    r = requests.get("https://raw.githubusercontent.com/ThatError404/EPM/main/Packages/packages").text
    # Split each line by letters and split packages by letters and see which package has the most matches of letters
    packages = r.split("\n")
    max = 0
    for i in packages:
        count = 0
        for j in i:
            if j == package[count]:
                count += 1
            else:
                break
        if count > max:
            max = count
            max_package = i
    if max == 0:
        print("\nNo packages found.")
        os.system(sys.executable + " main.py")
    else:
        print("\Closest match. " + max_package + ".")
        os.system(sys.executable + " main.py")

elif cmd == "exit":
    sys.exit()
