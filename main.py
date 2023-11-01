import requests
import json
import pandas as pd
import matplotlib.pyplot as plt

#Basically, I want you to build something in python that will access the API, grab historical data (can be past year, past 30 days, etc. Just choose something), and also the 7-day forecast. Then, display it as a plot using matplotlib.pyplot
#Order of how to go about it should be:
#1) Access the API and query the data you want
#2) Load the data into a pandas dataframe
#3) Drop unnecessary columns
#4) Do any necessary transformations (like if youre showing monthly/weekly averages)
#5) Display the dataframe as a plot using matplotlib

param1 = {
    "key": "1ba2706b9eef4a2483a173135232110",
    "q": "Houston",
    "days": "14"
}

url1 = 'http://api.weatherapi.com/v1/forecast.json'

response1 = requests.get(url1, params=param1)

if response1.status_code == 200:
    forecast_data = response1.json()
else:
    print("Error in API request")
    

# Seven-Day Forecast

dates = []
max_temperatures = []
min_temperatures = []
avg_temperatures = []
avg_humidity = []


for forecast in forecast_data['forecast']['forecastday']:
    date = forecast['date']
    max_temp = forecast['day']['maxtemp_f']
    min_temp = forecast['day']['mintemp_f']
    avg_temp = forecast['day']['avgtemp_f']
    avg_humd = forecast['day']['avghumidity']

    dates.append(date)
    max_temperatures.append(max_temp)    
    min_temperatures.append(min_temp)
    avg_temperatures.append(avg_temp)
    avg_humidity.append(avg_humd)

forecast_df = pd.DataFrame({
    'Dates': dates,
    'Max Temperatures': max_temperatures,
    'Min Temperatures': min_temperatures,
    "Average Temperatures": avg_temperatures,
    "Average Humidity": avg_humidity
})

print(forecast_df)


# Visualization of the forecast data
fig,ax = plt.subplots()
ax.set_title('7 Day Forecast')
ax.set_xlabel('Date')
ax.set_ylabel('Temperature (F)')

ax.plot(forecast_df['Dates'], forecast_df['Max Temperatures'], label = "Max Temp")
ax.plot(forecast_df['Dates'], forecast_df['Min Temperatures'], label = "Min Temp")
ax.plot(forecast_df['Dates'], forecast_df['Average Temperatures'], label = "Avg Temp")
ax.plot(forecast_df['Dates'], forecast_df['Average Humidity'], label = "Avg Humidity")
ax.legend(loc = 'best')
plt.show()

# Yearly Weather Data

param2 = {
    "key": "1ba2706b9eef4a2483a173135232110",
    "q": "Houston",
    "dt": "2023-01-01",
    "end_dt": "2023-01-31"
}

url2 = 'http://api.weatherapi.com/v1/history.json'
response2 = requests.get(url2,params=param2)

if response2.status_code == 200:
    historical_data = response2.json()
else:
    print(response2.status_code)
    print("Error in API request")


# January 01, 2023 - November 01, 2023

hist_dates = []
hist_max_temperatures = []
hist_min_temperatures = []
hist_avg_temperatures = []
hist_avg_humidity = []


for historical in historical_data['forecast']['forecastday']:
    date = historical['date']
    max_temp = historical['day']['maxtemp_f']
    min_temp = historical['day']['mintemp_f']
    avg_temp = historical['day']['avgtemp_f']
    avg_humd = historical['day']['avghumidity']

    hist_dates.append(date)
    hist_max_temperatures.append(max_temp)    
    hist_min_temperatures.append(min_temp)
    hist_avg_temperatures.append(avg_temp)
    hist_avg_humidity.append(avg_humd)

historical_df = pd.DataFrame({
    'Dates': hist_dates,
    'Max Temperatures': hist_max_temperatures,
    'Min Temperatures': hist_min_temperatures,
    "Average Temperatures": hist_avg_temperatures,
    "Average Humidity": hist_avg_humidity
})

print(historical_df)

# Visualization of Historical Data
fig,ax = plt.subplots()
ax.set_title('Weather from Jan - Nov 2023')
ax.set_xlabel('Date')
ax.set_ylabel('Temperature (F)')

ax.plot(historical_df['Dates'], historical_df['Max Temperatures'], label = "Max Temp")
ax.plot(historical_df['Dates'], historical_df['Min Temperatures'], label = "Min Temp")
ax.plot(historical_df['Dates'], historical_df['Average Temperatures'], label = "Avg Temp")
ax.plot(historical_df['Dates'], historical_df['Average Humidity'], label = "Avg Humidity")
ax.legend(loc = 'best')
plt.show()


