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
print(vacdata)
