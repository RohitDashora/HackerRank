import requests
import json
import datetime

#def __main__():
endpoint = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode=313001&date=03-05-2021'
pincode='313001'
date='03-05-2021'
url=endpoint+'pincode='+pincode+'&date='+date
print(url)
response=requests.get(url)
vacdata=response.json()


center_count =len(vacdata["centers"])


for i in range(0,center_count):
    sessions = vacdata["centers"][i]["sessions"]
    location = vacdata["centers"][i]["name"]
    freepaid =vacdata["centers"][i]["fee_type"]
    available=0
    for i in range(len(sessions)):
        min_age_limit =sessions[i]["min_age_limit"]
        available=sessions[i]["available_capacity"]
        slot= sessions[i]["slots"]
        if min_age_limit == 18 & available > 0 :
            print(location,freepaid, slot,available)



