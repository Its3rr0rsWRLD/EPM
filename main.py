import requests
import time
import sys
import os

cmd = input()
if cmd.find("epm install") != -1:
    package = cmd.split("epm install ")[1]
    rd = requests.get("https://raw.githubusercontent.com/ThatError404/EPM/main/Packages/" + package + "/required")
    if rd.status_code == 404:
        print("\nError: Package not found.")
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

elif cmd.find("epm uninstall") != -1:
    package = cmd.split("epm uninstall ")[1]
    if not os.path.exists(package):
        print("\nError: Package not found.")
    else:
        print("\nUninstalling " + package)
        os.system("rmdir /S /Q " + package)
        print("\n" + package + " uninstalled.\n")

elif cmd.find("epm search") != -1:
    package = cmd.split("epm search ")[1]
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
    else:
        print("\nClosest match. " + max_package + ".")

elif cmd.find("epm-npm ") != -1:
    package = cmd.split("epm-npm ")[1]
    print("\n(Running through Node Package Manager)\n")
    time.sleep(1)
    os.system("npm " + package)
elif cmd == "exit":
    sys.exit()