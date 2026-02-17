# Simple Weather App
# Enter your OpenWeatherMap API key below
API_KEY = "b9c7cc4bd45bbd4b595259d1aca8e1fd"

import requests
from datetime import datetime

def get_weather(city, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather = data['weather'][0]
        sys = data.get('sys', {})
        sunrise = sys.get('sunrise')
        sunset = sys.get('sunset')
        # Convert UNIX timestamps to readable time
        sunrise_time = datetime.fromtimestamp(sunrise).strftime('%H:%M:%S') if sunrise else 'N/A'
        sunset_time = datetime.fromtimestamp(sunset).strftime('%H:%M:%S') if sunset else 'N/A'
        print(f"Weather in {city}:")
        print(f"{weather['main']} - {weather['description']}")
        print(f"Temperature: {main['temp']}°C")
        print(f"Humidity: {main['humidity']}%")
        print(f"Pressure: {main['pressure']} hPa")
        print(f"Sunrise: {sunrise_time}")
        print(f"Sunset: {sunset_time}")

        # Try to get AQI (Air Quality Index) if possible
        coord = data.get('coord')
        if coord:
            lat, lon = coord.get('lat'), coord.get('lon')
            aqi_url = f"https://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={api_key}"
            aqi_response = requests.get(aqi_url)
            if aqi_response.status_code == 200:
                aqi_data = aqi_response.json()
                aqi = aqi_data['list'][0]['main']['aqi']
                aqi_meaning = {1: 'Good', 2: 'Fair', 3: 'Moderate', 4: 'Poor', 5: 'Very Poor'}
                print(f"Air Quality Index: {aqi} ({aqi_meaning.get(aqi, 'Unknown')})")
            else:
                print("Air Quality Index: Not available")
        else:
            print("Air Quality Index: Not available")
    else:
        print("City not found or API error.")

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city, API_KEY)
