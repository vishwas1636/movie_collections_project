import requests
from requests.auth import HTTPBasicAuth
import os
import logging
from dotenv import load_dotenv

# it will load environment variables from .env file
load_dotenv()

MOVIE_API_URL = "https://demo.credy.in/api/v1/maya/movies/"

def fetch_movies(page=1):
    username = os.getenv('MOVIE_API_USERNAME')
    password = os.getenv('MOVIE_API_PASSWORD')
    try:
        response = requests.get(MOVIE_API_URL, params={'page': page}, auth=HTTPBasicAuth(username, password), verify=False)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to fetch movies from API: {e}")
        raise e

