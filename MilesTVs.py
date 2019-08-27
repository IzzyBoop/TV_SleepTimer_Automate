import subprocess

print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("----------------------TV Automation Script-----------------------")
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("")
print("            ______________")
print("            |            | 1.  172.xx.xx.xxx   13. 172.xx.xx.xxx")
print("            |   Striven  | 2.  172.xx.xx.xxx   14. 172.xx.xx.xxx")
print("            |            | 3.  172.xx.xx.xxx")
print("    MAP     |        1   | 4.  172.xx.xx.xxx")
print("            |        -   | 5.  172.xx.xx.xxx")
print("            |        2   | 6.  172.xx.xx.xxx")
print("____________|_______     | 7.  172.xx.xx.xxx")
print("|                        | 8.  172.xx.xx.xxx")
print("|     T1        Proj.    | 9.  172.19.17.18")
print("|     3           5      | 10. 172.19.16.204")
print("|     -           -      | 11. 172.xx.xx.xxx")
print("|     4           6      | 12. 172.xx.xx.xxx")
print("|                        |___________________________________")
print("|                                                           |")
print("|     T3            T4       Software           Web         |")
print("|    7-8           9-10       11-12            13-14        |")
print("|     T2            T5        Indigo            Mktg        |")
print("|___________________________________________________________|")
print("")

while True:
    tvSelect = input("Make a TV Selection: ")

    tvArr = ["172.19.17.18","172.xx.xx.xx2","more","another","anotha one"]
    try:
        inputInt = int(tvSelect)
        tvArrNum = inputInt - 1

        if inputInt < 1 or inputInt > 14:
            print("Please select a number from 1-14")
        else:
            print("the command runs, good job, nerd.")
            tv = tvArr[tvArrNum]
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
        print("Input has to be a number.")
