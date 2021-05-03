import requests
import json
import datetime
from datetime import date
from datetime import timedelta

endpoint = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?'
ageLimit=45 #chnage it to 18
pincode='313001'
#date='03-05-2021'

def pollURL(endpoint, pincode, date):
    url=endpoint+'pincode='+pincode+'&date='+date
    #print(url)
    response=requests.get(url)
    return(response)


if __name__ == '__main__':
    
    dates=[]
    for i in range(0,8):
        d= date.today()+timedelta(days=i) 
        dates.append(d.strftime("%d-%m-%Y"))

    #lets get data for next 1 week

    slot_list =[]
    for date in dates :
        response = pollURL(endpoint, pincode, date)    
        vacdata=response.json()
        #print(vacdata)
        center_count =len(vacdata["centers"])
        for i in range(0,center_count):
            sessions = vacdata["centers"][i]["sessions"]
            location = vacdata["centers"][i]["name"]
            freepaid =vacdata["centers"][i]["fee_type"]
           
            for i in range(len(sessions)):
                session_list=[]
                min_age_limit =sessions[i]["min_age_limit"]
                available=sessions[i]["available_capacity"]
                slot= sessions[i]["slots"]
                if min_age_limit == ageLimit and available > 0 :
                    session_list.append(sessions[i]["date"])
                    session_list.append(location)
                    session_list.append(freepaid)
                    session_list.append(sessions[i]["vaccine"])
                    session_list.append(slot)
                    session_list.append(available)
                    slot_list.append(session_list)
    print(*slot_list, sep='\n')



