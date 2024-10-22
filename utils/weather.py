import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

def get_weather(city):
    city = city.strip()
    if not city:
        return "City name cannot be empty."
    
    # Correctly constructing the weather URL
    weather_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={WEATHER_API_KEY}"
    
    try:
        response = requests.get(weather_url)
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()

        # Check if the API response has the necessary keys
        if 'weather' in data and 'main' in data and 'wind' in data:
            weather = data['weather'][0]['description'].capitalize()  # More detailed description
            temp = round(data['main']['temp'])
            humidity = data['main']['humidity']
            wind_speed = round(data['wind']['speed'])
            
            return (
                f"The weather in {city} is: {weather}. "
                f"Temperature: {temp}ºF, Humidity: {humidity}%, Wind Speed: {wind_speed} mph."
            )
        else:
            return f"No weather data found for {city}. Response: {data}"

    except requests.exceptions.HTTPError as errh:
        return f"Http Error: {errh}"
    except requests.exceptions.ConnectionError as errc:
        return f"Error Connecting: {errc}"
    except requests.exceptions.Timeout as errt:
        return f"Timeout Error: {errt}"
    except requests.exceptions.RequestException as err:
        return f"An error occurred: {err}"
