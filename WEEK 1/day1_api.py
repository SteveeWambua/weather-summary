# Today's Exercise
#Fetch live data from a free public API and print a clean, human-readable summary. 
# Do not just print the raw JSON.
#You can use REST Countries or pick one of these free APIs that need no sign-up:
#Open-Meteo (open-meteo.com): free weather data, no key needed
#JSONPlaceholder (jsonplaceholder.typicode.com): fake user and post data for testing
#CoinGecko (api.coingecko.com): crypto prices, no key on free tier
#Your output should be readable by someone who does not know what JSON is.
#  Print labels. Format numbers. Make it clean.
#Push the file to GitHub when done.

import requests

# Nairobi coordinates
latitude = -1.2864
longitude = 36.8172

url = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": latitude,
    "longitude": longitude,
    "current": "temperature_2m,relative_humidity_2m,"
               "apparent_temperature,is_day,precipitation,"
               "wind_speed_10m",
    "timezone": "Africa/Nairobi"
}

try:
    response = requests.get(url, params=params, timeout=15)
    response.raise_for_status()
    data = response.json()

    current = data["current"]
    units = data["current_units"]

    print("\n====== NAIROBI WEATHER REPORT ======")
    print(f"Location: Nairobi, Kenya")
    print(f"Date and time: {current['time']}")
    print(
        f"Temperature: {current['temperature_2m']}"
        f"{units['temperature_2m']}"
    )
    print(
        f"Feels like: {current['apparent_temperature']}"
        f"{units['apparent_temperature']}"
    )
    print(
        f"Humidity: {current['relative_humidity_2m']}"
        f"{units['relative_humidity_2m']}"
    )
    print(
        f"Wind speed: {current['wind_speed_10m']}"
        f"{units['wind_speed_10m']}"
    )
    print(
        f"Precipitation: {current['precipitation']}"
        f"{units['precipitation']}"
    )

    daylight = "Yes" if current["is_day"] else "No"
    print(f"Is it daytime? {daylight}")
    print("====================================")

except requests.exceptions.RequestException as error:
    print(f"Could not retrieve weather data: {error}")

except (KeyError, ValueError) as error:
    print(f"Could not process the weather data: {error}")