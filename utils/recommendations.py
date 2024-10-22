import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

YELP_API_KEY = os.getenv("YELP_API_KEY")
TMDB_API_KEY = os.getenv("TMDB_API_KEY")

# Function to provide recommendations
def get_recommendations(category):
    recommendations = {
        "restaurants": "Here are some recommended restaurants: Restaurant A, Restaurant B, Restaurant C.",
    }
    return recommendations.get(category, "No recommendations available for this category.")

# Function to get Yelp recommendations for restaurants
def get_restaurant_recommendations(city):
    headers = {
        "Authorization": f"Bearer {YELP_API_KEY}"
    }
    url = f"https://api.yelp.com/v3/businesses/search?term=restaurants&location={city}&limit=5"
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()

        recommendations = []
        for business in data['businesses']:
            name = business['name']
            rating = business['rating']
            address = ", ".join(business['location']['display_address'])
            recommendations.append(f"**{name}** - Rating: {rating}/5\nLocation: {address}")
        
        return "\n\n".join(recommendations)
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"

# Function to get movie recommendations from TMDB
def get_movie_recommendations(genre=None, year_filter=None):
    # TMDB base URL for movies
    base_url = "https://api.themoviedb.org/3/discover/movie"
    
    # Genre IDs for TMDB (you can expand this as needed)
    genre_ids = {
        "Action": 28,
        "Comedy": 35,
        "Drama": 18,
        "Horror": 27,
        "Science Fiction": 878,
        "Romance": 10749,
        "Thriller": 53
    }
    
    # Prepare the parameters for the API request
    params = {
        "api_key": TMDB_API_KEY,
        "language": "en-US",
        "sort_by": "popularity.desc",
        "page": 1
    }
    
    # Add genre filter if selected
    if genre and genre in genre_ids:
        params["with_genres"] = genre_ids[genre]
    
    # Add year filter based on user input
    if year_filter == "After 2000":
        params["primary_release_date.gte"] = "2000-01-01"
    elif year_filter == "Before 2000":
        params["primary_release_date.lte"] = "1999-12-31"
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()

        recommendations = []
        for movie in data['results'][:5]:  # Limit to 5 movies
            title = movie['title']
            overview = movie['overview']
            release_date = movie.get('release_date', 'Unknown')
            recommendations.append(f"**{title}** (Released: {release_date}): {overview}")
        
        return "\n\n".join(recommendations)
    
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"
