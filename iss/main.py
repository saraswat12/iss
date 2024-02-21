import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL = "garimasaraswat85@gmail.com"
PASSWORD = "kgamnxwhzzaddqep" #kgam nxwh zzad dqep

MY_LAT = 27.177767250000002
MY_lng = 78.38972373047994

def iis_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iis_latitude = float(data["iss_position"]["latitude"])
    iis_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT-5 <= iis_latitude <= MY_LAT+5 and MY_lng-5 <= iis_longitude <= MY_lng+5:
        return True
                         


def night():
    parameters={
        "lat" : MY_LAT,
        "lng" : MY_lng,
        "formatted": 0,    
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True
while True:
    time.sleep(60)
    if iis_overhead() and night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=My_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:Look UP\n\nThe ISS is above you in the sky.")
        

#print(sunrise)
#print(sunset)
#print(time_now.hour)
