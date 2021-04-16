import os
import requests

def leavefunc():
    leave = input("Continue? y or n > ")
    if leave == "y":
        os.system("py main.py")


def functionclear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


url = "https://ipv4bot.whatismyipaddress.com/"
response = requests.get(url).text

print(f'''
IPv4: {response}
''')

userinput = input("Would you like to track this IPv4 Address? y or n > ")
if userinput == "y":
    res = requests.get("https://vpnapi.io/api/").text
    print(res)
    leavefunc()
else:
    print("Incorrect Command!")
    wrong = input("Continue? y or n > ")
    if wrong == "y":
        os.system("py Scripts/Vault/Python/ipv4.py")