from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Set up OpenAI API Key
client = OpenAI(api_key=OPENAI_API_KEY)

# Function to categorize user inquiries
def categorize_query(user_input):
    prompt = (
        f"Categorize the following inquiry into one of the categories: "
        f"scheduling, reminders, information retrieval, task management, general assistance, or general knowledge.\n"
        f"Inquiry: \"{user_input}\"\nCategory:"
    )
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    
    category = response.choices[0].message.content.strip()
    return category
