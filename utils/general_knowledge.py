from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Set up OpenAI API Key
client = OpenAI(api_key=OPENAI_API_KEY)

# Function to handle general knowledge queries
def get_general_knowledge_response(user_input):
    prompt = (
        f"Provide a detailed response to the following question:\n"
        f"Question: \"{user_input}\"\n"
    )
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    
    return response.choices[0].message.content.strip()
