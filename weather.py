##9/7/1942
import requests
r = requests.get('http://api.wunderground.com/api/19dacc4d3243ba55/history_19500101/q/SC/Greenville_Downtown.json')
json = r.json()
maxTemp = json['history']['dailysummary'][0]['maxtempi']
minTemp = json['history']['dailysummary'][0]['mintempi']
year = json['history']['dailysummary'][0]['date']['year']
month = json['history']['dailysummary'][0]['date']['mon']
day = json['history']['dailysummary'][0]['date']['mday']
print("Date: " + month + "/" + day + "/" + year + " Max: " + maxTemp + " Min: " + minTemp)
r.close()