# Made by https://github.com/0x1CA3

import os
import ctypes

ctypes.windll.kernel32.SetConsoleTitleW("[GetWiFiPwd]")

def functionclear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
functionclear()

print(''' 
    ╦ ╦┬┌─┐┬╔═╗┬ ┬┌┬┐
    ║║║│├┤ │╠═╝│││ ││
    ╚╩╝┴└  ┴╩  └┴┘─┴┘
-------------------------
Use !help for commands.
''')

userinput = input("WifiPwd > ")
if userinput == "!help":
    print(''' 
    !help - Prints out help commands.
    !dump - Dumps out wifi credentials.
    !back - Goes back to The Vault.
    ''')
    meninput = input("Continue? y or n > ")
    if meninput == "y":
        os.system("py Scripts/Vault/Python/getwifipwd.py")
elif userinput == "!dump":
    os.system("Netsh WLAN show profiles")
    print(''' 
    Pick a Wi-Fi Network from above
    to dump passwords from.
    ''')
    wifiinput = input("Pick a network > ")
    os.system("NETSH WLAN SHOW PROFILE {} KEY=CLEAR".format(wifiinput))
    print(''' 
    Look at 'Key content' under the 'Security settings' section
    for the Wi-Fi password.
    ''')
    meninput11 = input("Continue? y or n > ")
    if meninput11 == "y":
        os.system("py Scripts/Vault/Python/getwifipwd.py")
elif userinput == "!back":
    os.system("py Scripts/Vault/vault.py")
else:
    print("Incorrect Command!")
    wronginputt = input("Continue? y or n")
    if wronginputt == "y":
        os.system("py Scripts/Vault/Python/getwifipwd.py")