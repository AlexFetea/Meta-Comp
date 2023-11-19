import pandas as pd
from actors import get_person_popularity
import json
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm

# Read the CSV file
df = pd.read_csv('./data/netflix_titles.csv')

# Extract unique names of directors and actors
directors = df['director'].dropna().unique()
actors = df['cast'].dropna().unique()

# Flatten the list of actors
actors_list = [actor for sublist in actors for actor in sublist.split(', ')]

# Combine and get unique names
unique_names = set(list(directors) + actors_list)

# Dictionary to store popularity scores
popularity_scores = {}

def clean_name(name):
    if not isinstance(name, str):
        return name

    try:
        # Try decoding with utf-8
        cleaned_name = name.encode('utf-8', 'ignore').decode('utf-8')
    except UnicodeEncodeError:
        try:
            # Try decoding with latin1
            cleaned_name = name.encode('latin1').decode('utf-8')
        except UnicodeEncodeError:
            # Default to the original name if other decodings fail
            cleaned_name = name

    return cleaned_name.strip()

flattened_names = []
for name in unique_names:
    split_names = name.split(', ')
    flattened_names.extend(split_names)

import numpy
a = numpy.asarray(flattened_names)
with open("./data/names.csv", "w", encoding="utf-8") as f:
    numpy.savetxt(f, a, delimiter=",", fmt='%s')
