import requests
import webbrowser
from colorama import init, Fore
import os
import hashlib
import time
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
time2 = "["+Fore.CYAN+current_time+Fore.WHITE+"] "

init(convert=True)

def auth():
    filename = 'authkey.txt'
    if os.path.isfile(filename):
        hasher = hashlib.md5()
        with open(filename, 'rb') as open_file:
            content = open_file.read()
            hasher.update(content)
        req=requests.get("https://www.nulled.to/misc.php?action=validateKey&authKey=" + hasher.hexdigest())
        if "auth\":true}" in req.text:
            print(time2 + Fore.GREEN + "Auth granted! Welcome!" + Fore.RESET)
            time.sleep(3)
        else: 
            print(time2 + Fore.RED + "Inavlid auth key! Get one from https://nulled.to/auth.php ! Closing...")
            time.sleep(3)
            exit()
    else:
        print(time2 + "Enter your auth key:" + Fore.RESET)
        authkey = str(input())
        hasher = hashlib.md5()
        hasher.update(authkey.encode('utf-8'))
        req=requests.get("https://www.nulled.to/misc.php?action=validateKey&authKey=" + hasher.hexdigest())
        if "auth\":true}" in req.text:
            f = open('authkey.txt', 'w')
            f.write(authkey)
            print(time2 + Fore.GREEN + "Auth granted! Welcome!" + Fore.RESET)
            time.sleep(3)
        else: 
            print(time2 + Fore.RED + "Inavlid auth key! Get one from https://nulled.to/auth.php ! Closing...")
            time.sleep(3)
            exit()
def mycode():
   print("")
if __name__ == "__main__":
    auth()
    mycode() 
title = """
 /\   /\___  _ __   __| | / _\ ___ _ __ __ _ _ __   ___ _ __
 \ \ / / _ \| '_ \ / _` | \ \ / __| '__/ _` | '_ \ / _ \ '__|
  \ V / (_) | | | | (_| | _\ \ (__| | | (_| | |_) |  __/ |
   \_/ \___/|_| |_|\__,_| \__/\___|_|  \__,_| .__/ \___|_|
                                            |_| V1
Made by VonD
BTC: 1Hexziesm44sETfs3BZfwrB81Q4RvBkCQG

"""

print(title)
print("Choose the type of proxy:")
print("[1] HTTP/S")
print("[2] SOCKS4")
print("[3] SOCKS5")
print(           )
proxy = input("Type: ")
print(           )


if proxy == '1':
    http = requests.get("https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=5000&country=all&anonymity=anonymous,elite&ssl=all")
    with open('http_proxies.txt', 'wb') as b:
        b.write(http.content)
    print("Finished Scraping")
    webbrowser.open("https://www.nulled.to/user/3721496-vond")
    b.close()
elif proxy == '2':
    socks4 = requests.get("https://api.proxyscrape.com/?request=getproxies&proxytype=socks4&timeout=5000&country=all&anonymity=anonymous,elite&ssl=all")
    with open('SOCKS4.txt', 'wb') as c:
        c.write(socks4.content)
    print("Finished Scraping")
    webbrowser.open("https://www.nulled.to/user/3721496-vond")
    c.close()
elif proxy == '3':
    socks5 = requests.get("https://api.proxyscrape.com/?request=getproxies&proxytype=socks5&timeout=5000&country=all&anonymity=anonymous,elite&ssl=all")
    with open('SOCKS5.txt', 'wb') as d:
        d.write(socks5.content)
    print("Finished Scraping")
    webbrowser.open("https://www.nulled.to/user/3721496-vond")
    d.close()
else:
    print("Invalid Type!")

    raise SystemExit
