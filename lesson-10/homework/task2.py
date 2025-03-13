import requests
import random

def get_genre_id(genre_name, api_key):
    url = f"https://api.themoviedb.org/3/genre/movie/list?api_key={api_key}&language=en-US"
    response = requests.get(url)
    
    if response.status_code != 200:
        return None  # Return None if the request fails
    
    try:
        genres = response.json().get("genres", [])
        for genre in genres:
            if genre["name"].lower() == genre_name.lower():
                return genre["id"]
    except KeyError:
        return None  # Handle unexpected response format
    
    return None  # Return None if the genre is not found
def get_movies_by_genre(genre_id, api_key):
    url = f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}&with_genres={genre_id}"
    response = requests.get(url)
    
    if response.status_code != 200:
        return []  # Return an empty list if the request fails
    
    try:
        return response.json().get("results", [])
    except KeyError:
        return []  # Handle unexpected response format

def recommend_movie(genre_name, api_key):
    genre_id = get_genre_id(genre_name, api_key)
    
    if genre_id is None:
        return f"Genre '{genre_name}' not found or API request failed."
    
    movies = get_movies_by_genre(genre_id, api_key)
    
    if not movies:
        return f"No movies found for genre '{genre_name}'."
    
    movie = random.choice(movies)
    return f"Recommended Movie: {movie.get('title', 'Unknown Title')} (Rating: {movie.get('vote_average', 'N/A')})"

# Replace 'your_api_key_here' with your actual TMDB API key
API_KEY = "your_api_key_here"

# User input for genre
genre_name = input("Enter a movie genre: ").strip()
print(recommend_movie(genre_name, API_KEY))
