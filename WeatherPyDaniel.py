
# coding: utf-8

# In[130]:


#import dependencies
import matplotlib.pyplot as plt
import pandas as pd
import json
import time
import requests
import pprint
import codecs
import random
from config import weatherApiKey

#randomly select 500 cities from the city list (saved as txt but is .json format)
file = "city.list.json"
cities = json.load(codecs.open(file, 'r', 'utf-8-sig')) #the codecs package is needed because of the way the json filew was created. Would get the following error: Unexpected UTF-8 BOM (decode using utf-8-sig): line 1 column 1 (char 0)
#len(cities) #provides 209579 cities

def ListCreator(data,list):
    for i in data:
        list.append(i['id'])       

CityIdList = []
ListCreator(cities, CityIdList)
CitySample = random.sample(CityIdList, 500)


# In[131]:


#for each city, find its temperature, wind speed, humidity, cloudiness and latitude
#download this information from openweathermap.org
variables = ['id','city', 'country',  'lon', 'lat', 'tempMax', 'windSpd', 'humidity', 'cloudiness']
base = 'http://api.openweathermap.org/data/2.5/weather?APPID='+ weatherApiKey

df = pd.DataFrame(columns = variables)
#build for loop to run through the city list
for i in CitySample:
    city = str(i)
    url = base + '&id=' + city
    data = requests.get(url).json()
    name = data['name']
    print(f'looking up data for {name}')
    country = data['sys']['country']
    lon = data['coord']['lon']
    lat = data['coord']['lat']
    tempMax = (((data['main']['temp_max'])- 273.15) * 9/5 + 32) #kelvin to Farenheit
    windSpd = data['wind']['speed']
    humidity = data['main']['humidity']
    cloudiness = data['clouds']['all']
    row = [city, name, country, lon, lat, tempMax, windSpd, humidity, cloudiness]

    tempdf = pd.DataFrame([row], columns = variables)
    #store this data as a dataframe
    df = df.append(tempdf)
    
#print(df)


# In[141]:



#build scatterplots:
# Temperature (F) vs. Latitude
plt.scatter(df['lat'], df['tempMax'], s=1.5)
plt.xlabel("Latitude")
plt.ylabel("Temperature")
plt.show()

#print(df.head())


# In[142]:


# Humidity (%) vs. Latitude
plt.scatter(df['lat'], df['humidity'], s=1.5)
plt.xlabel("Latitude")
plt.ylabel("Humidity")
plt.show()


# In[146]:


# Cloudiness (%) vs. Latitude
plt.scatter(df['lat'], df['humidity'], s=1.5)
plt.xlabel("Latitude")
plt.ylabel("Humidity")
plt.show()


# In[147]:


# Wind Speed (mph) vs. Latitude
plt.scatter(df['lat'], df['windSpd'], s=1.5)
plt.xlabel("Latitude")
plt.ylabel("Wind Speed")
plt.show()


# In[148]:


plt.scatter(df['humidity'], df['windSpd'], s=1.5)
plt.xlabel("Humidity")
plt.ylabel("Wind Speed")
plt.show()

