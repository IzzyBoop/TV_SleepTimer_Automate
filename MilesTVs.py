import subprocess

print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("---------------------TV Sleep Timer Script-----------------------")
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("(Requires ADB to run)")
#im a fricken arteest
print("")
print("                         ___________________")
print("                         |     |/   \|     |")
print("                         | 18              |")
print("                         | 17    LOBBY     |")
print("                         | 16              |")
print("                         | 15              |")
print("            _____________|_________________|")
print("            |            | 1.  172.19.16.10     13. 172.19.16.69")
print("            |   Striven  | 2.  172.19.16.12     14. 172.19.16.27")
print("            |            | 3.  172.19.16.36     15. 172.19.23.219")
print("    MAP     |        1   | 4.  172.19.16.28     16. 172.19.20.152")
print("            |        -   | 5.  172.19.16.211    17. 172.19.16.8")
print("            |        2   | 6.  172.19.16.212    18. 172.19.23.195")
print("____________|_______     | 7.  172.19.16.7")
print("|                        | 8.  172.19.16.16")
print("|     T1        Proj.    | 9.  172.19.17.18")
print("|     3           5      | 10. 172.19.16.204")
print("|     -           -      | 11. 172.19.16.11")
print("|     4           6      | 12. 172.19.16.245    0. Manual Input")
print("|                        |___________________________________")
print("|                                                           |")
print("|     T3            T4       Software           Web         |")
print("|    7-8           9-10       11-12            13-14        |")
print("|     T2            T5        Indigo            Mktg        |")
print("|___________________________________________________________|")
print("")

while True:
    tvSelect = input(">Make a TV Selection (Ctrl-C to quit): ")

    # First 2 octets are always the same so array is just last 2 of IPs
    tvArr = [
    "16.10",
    "16.12",
    "16.36",
    "16.28",
    "16.211",
    "16.212",
    "16.7",
    "16.16",
    "16.18",
    "16.204",
    "16.11",
    "16.245",
    "16.69",
    "16.27",
    "23.219",
    "20.152",
    "16.8",
    "23.195"
    ]

    def ADB_Function(tv):
        tvPort = "5555"
        print("Attempting adb connect on " + tv + ":" + tvPort)
        adbConnect = subprocess.check_output("adb connect " + tv + ":" + tvPort).decode('utf-8')
        print(adbConnect)
        print("Attempting db shell settings put secure sleep_timeout 0 on " + tv + ":" + tvPort)
        slpTimer = subprocess.check_output("adb shell settings put secure sleep_timeout 0").decode('utf-8')
        print(slpTimer)
        print("Attempting adb shell settings put system screen_off_timeout 2147460000 on " + tv + ":" + tvPort)
        scrnOff = subprocess.check_output("adb shell settings put system screen_off_timeout 2147460000").decode('utf-8')
        print(scrnOff)
        print("Attempting adb disconnect on " + tv + ":" + tvPort)
        disconnect = subprocess.check_output("adb disconnect " + tv + ":" + tvPort).decode('utf-8')
        print(disconnect)
        print("Finished")

    try:
        inputInt = int(tvSelect)
        tvArrNum = inputInt - 1 #because array do the whole 0 thing

        if inputInt < 0 or inputInt > 18:
            print("***Please select a number from 0-18***")
        elif inputInt == 0:
            manInput = input("Please enter IP Address: ")
            tv = manInput
            ADB_Function(tv)
        else:
            tv = "172.19." + tvArr[tvArrNum]
            ADB_Function(tv)
    except:
        print("***Input has to be a number. (Or command failed)***")
        print("***If you did input a number then the command likely failed.***")
        print("***Can you contact the TV? Try pinging it. Are you on the proper wifi network?***")
        print("***Remember: The Wifi network needs to be opened up. Message Justin C.***")
        print("***If it failed right away with no delay, did you install ADB?***")
