import requests
import os
import time

os.system('cls' if os.name=='nt' else 'clear')
phone = input("Set Your Number Via +98==>\n\r")
def snap(phone):
  try:
    snapH = {"x-app-name":"passenger-android", "Package-Name":"cab.snapp.passenger.play", "locale":"fa-IR", "x-app-version-code":"207", "x-app-version":"207", "Content-Type":"application/json; charset=utf-8", "Host":"oauth-passenger.snapp.site", "Accept-Encoding":"gzip, deflate"}
    snapD = {"cellphone":phone}
    snapR = requests.post("https://oauth-passenger.snapp.site/v2/otp", headers=snapH, json=snapD)
    snapp = snapR.text
    if "OK" in snapp:
        print("Sended")
    else:
        print("Fuck!")
  except:
    time.sleep(60)
