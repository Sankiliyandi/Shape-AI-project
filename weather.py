import requests
from datetime import datetime
api_key='9d912fe7bd602a9819bc12369cd717f9'
location=input(("Enter the city name:"))
complete_api_link="https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
apiLink=requests.get(complete_api_link)
apiData=apiLink.json()


temp_city = ((apiData['main']['temp']) - 273.15)
weather_desc = apiData['weather'][0]['description']
hmdt = apiData['main']['humidity']
wind_spd = apiData['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print ("-------------------------------------------------------------")
print ("Weather Stats for - {}  || {}".format(location.upper(), date_time))
print ("-------------------------------------------------------------")

print ("Current temperature is: {:.2f} deg C".format(temp_city))
print ("Current weather desc  :",weather_desc)
print ("Current Humidity      :",hmdt, '%')
print ("Current wind speed    :",wind_spd ,'kmph')
