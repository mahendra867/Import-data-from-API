import requests
import csv

from requests.api import head 

url = "https://weatherapi-com.p.rapidapi.com/current.json"

querystring = {"q":"53.1,-0.13"}

headers = {
	"X-RapidAPI-Key": "d1fadc96b1msh17524134dc19511p129877jsne81e075f0211",
	"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

myjson = response.json()

ourdata = []
csvheader = ['NAME', 'REGION', 'COUNTRY', 'LAT', 'LON', 'TZ_ID', 'LOCALTIME_EPOCH', 'LOCAL_TIME']

for x in myjson['location']:
    listing = [x['name'], x['region'], x['country'], x['lat'], x['lon'], x['tz_id'], x['localtime_epoch'], x['localtime']]
    ourdata.append(listing)

with open('weather.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)

    writer.writerow(csvheader)
    writer.writerows(ourdata)

print('done')
