import requests
import json
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

CALENDARIFIC_API_KEY = os.getenv("CALENDARIFIC_API_KEY")

# Calendarific API URL
CALENDARIFIC_URL = "https://calendarific.com/api/v2/holidays"

# Function to fetch holidays using Calendarific API
def fetch_holidays(api_key, country, year, month, day):
    params = {
        'api_key': api_key,
        'country': country,
        'year': year,
        'month': month,
        'day': day,
    }
    try:
        response = requests.get(CALENDARIFIC_URL, params=params)
        data = response.json()
        if response.status_code == 200:
            holidays = data.get('response', {}).get('holidays', [])
            return holidays
        else:
            return f"Error fetching holidays: {data.get('error', {}).get('message', 'Unknown error')}"
    except Exception as e:
        return f"Error occurred: {str(e)}"
