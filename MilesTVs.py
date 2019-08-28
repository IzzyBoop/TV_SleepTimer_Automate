import subprocess

print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("----------------------TV Automation Script-----------------------")
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("                         ___________________")
print("                         | 18              |")
print("                         | 17    LOBBY     |")
print("                         | 16              |")
print("                         | 15              |")
print("            _____________|_________________|")
print("            |            | 1.  172.19.16.10     13. 172.19.16.69")
print("            |   Striven  | 2.  172.19.16.12     14. 172.19.16.27")
print("            |            | 3.  172.xx.xx.xxx    15. 172.19.23.219")
print("    MAP     |        1   | 4.  172.19.16.28     16. 172.19.20.152")
print("            |        -   | 5.  172.xx.xx.xxx    17. 172.19.16.8")
print("            |        2   | 6.  172.19.16.212    18. 172.19.23.195")
print("____________|_______     | 7.  172.19.16.7")
print("|                        | 8.  172.19.16.16")
print("|     T1        Proj.    | 9.  172.19.17.18")
print("|     3           5      | 10. 172.19.16.204")
print("|     -           -      | 11. 172.19.16.11")
print("|     4           6      | 12. 172.19.16.245")
print("|                        |___________________________________")
print("|                                                           |")
print("|     T3            T4       Software           Web         |")
print("|    7-8           9-10       11-12            13-14        |")
print("|     T2            T5        Indigo            Mktg        |")
print("|___________________________________________________________|")
print("")

while True:
    tvSelect = input("Make a TV Selection: ")

    tvArr = ["172.19.16.10",
    "172.19.16.12",
    "172.19.16.xxx",
    "172.19.16.28",
    "172.19.16.xxx",
    "172.19.16.212",
    "172.19.16.7",
    "172.19.16.16",
    "172.19.16.18",
    "172.19.16.204",
    "172.19.16.11",
    "172.19.16.245",
    "172.19.16.69",
    "172.19.16.27",
    "172.19.23.219",
    "172.19.20.152",
    "172.19.16.8",
    "172.19.23.195"]

    try:
        inputInt = int(tvSelect)
        tvArrNum = inputInt - 1

        if inputInt < 1 or inputInt > 18:
            print("Please select a number from 1-18")
        else:
            tv = tvArr[tvArrNum]
            print("the command runs, good job, nerd. TV IP: " + tv)
            one = subprocess.check_output("adb kill-server").decode('utf-8')
            print(one)
            two = subprocess.check_output("adb start-server").decode('utf-8')
            print(two)
            three = subprocess.check_output("adb connect " + tv).decode('utf-8')
            print(three)
            four = subprocess.check_output("adb shell settings put secure sleep_timeout 0").decode('utf-8')
            print(four)
            five = subprocess.check_output("adb shell settings put system screen_off_timeout 2147460000").decode('utf-8')
            print(five)
            six = subprocess.check_output("adb disconnect " + tv).decode('utf-8')
            print(six)
            seven = subprocess.check_output("adb kill-server").decode('utf-8')
            print(seven)
    except:
        print("Input has to be a number. (Or command failed)")
