import requests
import json
import timedelta

def schedule_meeting(user_email, meeting_datetime):
    # Define the URL for the scheduling API
    url = 'https://api.calendly.com/scheduled_events'

    # Calculate the end time for the meeting (30 minutes duration)
    start_time = meeting_datetime
    end_time = start_time + timedelta(minutes=30)

    # Define the payload for the meeting request
    payload = {
        "event": {
            "name": "Meeting with Ashish",
            "start_time": start_time.isoformat() + "Z",  # Use ISO format
            "end_time": end_time.isoformat() + "Z",
            "duration": 30,  # Duration in minutes
            "invitee": {
                "email": user_email
            }
        }
    }

    # Set the headers for authentication
    headers = {
        "Authorization": f"Bearer {CALENDLY_API_TOKEN}",
        "Content-Type": "application/json"
    }

    # Make the request to schedule the meeting
    response = requests.post(url, headers=headers, data=json.dumps(payload))

    if response.status_code == 201:
        return True, response.json()  # Return success and response JSON
    else:
        return False, response.text  # Return failure message
