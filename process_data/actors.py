import requests
import json



def get_person_popularity(name):
    # API endpoint for searching a person
    url = "https://api.themoviedb.org/3/search/person"

    # Your API key (Bearer token)
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzOTg5ODJiMDdhNGRkZWE4ZjBmOTI4NjRmMzU5MmVhOCIsInN1YiI6IjY1NWE3YjEwMjIyMmY2MDEzOTJhYzRmZSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.1YgoNj90nNur3bG7POfzZpcqEhDP92NRyCWk7k9QLa4"
    }

    # Parameters for the search
    params = {
        'api_key': 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzOTg5ODJiMDdhNGRkZWE4ZjBmOTI4NjRmMzU5MmVhOCIsInN1YiI6IjY1NWE3YjEwMjIyMmY2MDEzOTJhYzRmZSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.1YgoNj90nNur3bG7POfzZpcqEhDP92NRyCWk7k9QLa4',  # Replace with your actual API Key
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



