import requests
import csv

url ='http://api.coincap.io/v2/assets'

headers={
    'Accept': 'application/json',
    'Content-Type':'application/json'
}
response=requests.request("GET",url,headers=headers,data={})
myjson=response.json()
print(myjson)