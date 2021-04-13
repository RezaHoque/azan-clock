from datetime import date
import requests
import json
from datetime import datetime
from playsound import playsound
import gi
import time

today = date.today().strftime('%d-%m-%Y')
print("Today's date:", today)


data_from_api=requests.get(f'http://api.aladhan.com/v1/calendarByCity?city=copenhagen&country=denmark&method=4&month={datetime.today().month}&year={datetime.today().year}')
#print(r.json())
data=data_from_api.json()
print(data['status'])

for d in data['data']:
    if today==d['date']['gregorian']['date']:
        #print(d['date']['gregorian']['date'])
        #print(d['timings'])
        namaz_times_data=d['timings']
        namaz_times={}
        namaz_times[0]=namaz_times_data['Fajr'][0:5]
        namaz_times[1]=namaz_times_data['Dhuhr'][0:5]
        namaz_times[2]=namaz_times_data['Asr'][0:5]
        namaz_times[3]=namaz_times_data['Maghrib'][0:5]
        namaz_times[4]=namaz_times_data['Isha'][0:5]
        
        print(namaz_times)
        starttime = time.time()
        while True:
            print ("tick")
            time.sleep(60.0 - ((time.time() - starttime) % 60.0))
            
            current_time=datetime.now().strftime("%H:%M")#'20:08'
            for k,v in namaz_times.items():
                if current_time==v:
                    print('Its prayer time. Playing azan')
                    playsound('azan.mp3')
                
        
        
        

