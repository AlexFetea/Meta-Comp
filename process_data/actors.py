import requests
import json
import os



def get_person_popularity(name):
    # API endpoint for searching a person
    url = "https://api.themoviedb.org/3/search/person"

    # Fetch the API key from environment variables
    api_key = os.getenv('TMDB_API_KEY')

    # Your API key (Bearer token)
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    # Parameters for the search
    params = {
        'api_key': api_key,  # Use the API Key from the environment variable
        'query': name
    }

    response = requests.get(url, headers=headers, params=params)

    # Check the response status code
    if response.status_code != 200:
        print(f"Error fetching data for {name}: HTTP {response.status_code}")
        print("Response:", response.text)
        return None

    # Parse JSON data
    try:
        data = response.json()
        if data['results']:
            return data['results'][0]['popularity']
        else:
            return None
    except json.JSONDecodeError as e:
        print(f"JSON decoding error for {name}: {e}")
        return None



