import pandas as pd
import re
df = pd.read_csv('Frequency Lists/French/Raw.csv')
for column in ['French', 'English', 'POS']:
    df[column] = df[column].astype(str)
df['Rank'] = df['Rank'].astype(int)
# Create a dictionary to map Rank to French words
rank_to_french = df.set_index('Rank')['French'].to_dict()

# Function to replace the references in English column
def replace_references(text):
    # Find all instances of (see #x, x, x)
    matches = re.findall(r'\(see #(.*?)\)', text)
    for match in matches:
        # Split the references by comma and space
        numbers = match.split(', ')
        replacements = [rank_to_french[int(num)] for num in numbers if int(num) in rank_to_french]
        replacement_text = ', '.join(replacements)
        # Replace the (see #x, x, x) with (see French words)
        text = text.replace(f'(see #{match})', f'(see {replacement_text})')
    return text

# Apply the replacement function to the English column
df['English'] = df['English'].apply(replace_references)

def remove_references(text):
    return re.sub(r'\(see .*?\)', '', text).strip()

# Apply the function to the English column
df['English'] = df['English'].apply(remove_references)

def clean_text(text):
    text = text.replace('; languagedaily dot com;', ',').replace('french.languagedaily.com', '').replace('; languagedaily dot com', '').strip()
    # Remove any trailing or leading semicolons or commas
    text = re.sub(r'^[;,]|[;,]$', '', text).strip()
    return text

# Apply the function to the English column
df['English'] = df['English'].apply(clean_text)

df.to_csv('Frequency Lists/French/Clean.csv')
