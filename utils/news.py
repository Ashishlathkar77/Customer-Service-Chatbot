import requests

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")

def get_news():
    news_url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}"

    try:
        response = requests.get(news_url)
        response.raise_for_status()
        data = response.json()

        if 'articles' in data:
            summaries = []
            for article in data['articles']:
                title = article['title']
                description = article['description'] if article['description'] else "No description available."
                url = article['url']
                published_at = article['publishedAt']

                summaries.append(f"**{title}**: {description} \n*Published on: {published_at}*  \n[Read more]({url})")
            return "\n\n".join(summaries)
        else:
            return "No articles found."

    except requests.exceptions.HTTPError as errh:
        return f"Http Error: {errh}"
    except requests.exceptions.ConnectionError as errc:
        return f"Error Connecting: {errc}"
    except requests.exceptions.Timeout as errt:
        return f"Timeout Error: {errt}"
    except requests.exceptions.RequestException as err:
        return f"An error occurred: {err}"
