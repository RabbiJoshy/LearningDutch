import pandas as pd
import re
import os
language = 'Dutch'
df = pd.read_csv(os.path.join('Frequency Lists',language,'Raw.csv'))

# Function to extract the first POS
def extract_first_pos(translation):
    # parts = translation.split('.')
    # first_part = parts[0].strip()
    parts = translation.split(':')
    pos = parts[0]

    return pos.strip()

# Apply the function to create a new column
df['POS'] = df['GTPOSTRANS'].apply(extract_first_pos)

df.to_csv(os.path.join('Frequency Lists',language,'Clean.csv'))