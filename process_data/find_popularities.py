import pandas as pd
from actors import get_person_popularity
import json
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm

# Read the CSV file. Assuming the names are in the first column without a header.
names_series = pd.read_csv('./data/names.csv', header=None, squeeze=True)

# Convert the pandas Series to a list and take only the first 200 names
names_list = names_series.tolist()[:200]

def process_name(name):
    # Fetch popularity
    popularity = get_person_popularity(name)
    return name, popularity

popularity_scores = {}

# Using ThreadPoolExecutor to parallelize the process
with ThreadPoolExecutor(max_workers=30) as executor:
    # Map the function to the names and process asynchronously
    futures = {executor.submit(process_name, name): name for name in names_list}

    # Use tqdm to display progress
    for future in tqdm(as_completed(futures), total=len(names_list), desc="Fetching Popularity Scores"):
        name = futures[future]
        try:
            name, popularity = future.result()
            if popularity is not None:
                popularity_scores[name] = popularity
        except Exception as e:
            print(f"Error processing {name}: {e}")

# Save to JSON file
with open('./data/popularity_subset.json', 'w') as json_file:
    json.dump(popularity_scores, json_file)

print("Popularity scores for the subset saved to popularity_subset.json")
