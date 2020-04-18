import requests
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
    b.close()
elif proxy == '2':
    socks4 = requests.get("https://api.proxyscrape.com/?request=getproxies&proxytype=socks4&timeout=5000&country=all&anonymity=anonymous,elite&ssl=all")
    with open('SOCKS4.txt', 'wb') as c:
        c.write(socks4.content)
    print("Finished Scraping")
    c.close()
elif proxy == '3':
    socks5 = requests.get("https://api.proxyscrape.com/?request=getproxies&proxytype=socks5&timeout=5000&country=all&anonymity=anonymous,elite&ssl=all")
    with open('SOCKS5.txt', 'wb') as d:
        d.write(socks5.content)
    print("Finished Scraping")
    d.close()
else:
    print("Invalid Type!")

    raise SystemExit
