import requests
import os
import time
from threading import Thread

phone = input("Set Your Number Via +98==>\n\r")
snapH = {"x-app-name":"passenger-android", "Package-Name":"cab.snapp.passenger.play", "locale":"fa-IR", "x-app-version-code":"207", "x-app-version":"207", "Content-Type":"application/json; charset=utf-8", "Host":"oauth-passenger.snapp.site", "Accept-Encoding":"gzip, deflate"}
snapD = {"cellphone":phone}
snapR = requests.post("https://oauth-passenger.snapp.site/v2/otp", headers=snapH, json=snapD)

snap = snapR.text

if "OK" in snap:
  print("Sended")
else:
  print("Fuck!")
