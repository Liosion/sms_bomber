import requests

phone = str(input("Set Your Number Via +98==>\n\r"))
snapH = {"x-app-name":"passenger-android", "Package-Name":"cab.snapp.passenger.play", "locale":"fa-IR", "x-app-version-code":"207", "x-app-version":"207", "Content-Type":"application/json; charset=utf-8", "Host":"oauth-passenger.snapp.site", "Accept-Encoding":"gzip, deflate"}
snapD = {"cellphone":phone}
    try:
        snapR = requests.post("https://oauth-passenger.snapp.site/v2/otp", headers=snapH, json=snapD)
        if "OK" in snapR.text:
            print ("sended sms:)")
        else:
            print ("Error!")
    except:
	    print ("Error!")
