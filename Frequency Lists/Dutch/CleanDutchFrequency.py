import pandas as pd
import re
import os
language = 'Dutch'
import spacy
from deep_translator import GoogleTranslator
import time

df = pd.read_csv(os.path.join('Frequency Lists',language,'Raw.txt'), sep=" ")

# Load the spaCy model
nlp = spacy.load("nl_core_news_sm")

def add_spacy_POS_info(df):
    # Custom mapping for more understandable POS descriptions
    pos_mapping = {
        'ADJ': 'Adjective',
        'ADP': 'Preposition',
        'ADV': 'Adverb',
        'AUX': 'Auxiliary',
        'CONJ': 'Conjunction',
        'CCONJ': 'Conjunction',
        'DET': 'Determiner',
        'INTJ': 'Interjection',
        'NOUN': 'Noun',
        'NUM': 'Numeral',
        'PART': 'Particle',
        'PRON': 'Pronoun',
        'PROPN': 'Proper noun',
        'PUNCT': 'Punctuation',
        'SCONJ': 'Conjunction',
        'SYM': 'Symbol',
        'VERB': 'Verb',
        'X': 'Other'
    }

    # Initialize the Google translator
    translator = GoogleTranslator(source='nl', target='en')

    # Function to get POS, tag, layman's description, and translation
    def get_pos_tag_layman_translation(word):
        start_time = time.time()
        doc = nlp(word)
        pos, tag, layman_description = None, None, None
        for token in doc:
            pos = token.pos_
            tag = token.tag_
            layman_description = pos_mapping.get(pos, 'Unknown')
        translation = translator.translate(word)
        end_time = time.time()
        duration = end_time - start_time
        print(f"Translated '{word}' to '{translation}' in {duration:.4f} seconds")
        return pos, tag, layman_description, translation

    # Apply the function to each word in the DataFrame
    df[['SpaCy_POS', 'SpaCy_Tag', 'POS', 'Translation']] = df['Dutch'].apply(
        lambda word: pd.Series(get_pos_tag_layman_translation(word)))

    return df

df2 = add_spacy_POS_info(df)
df2.to_csv(os.path.join('Frequency Lists',language,'Clean.csv'))


# df = pd.read_csv(os.path.join('Frequency Lists',language,'Raw.csv'))
#
# # Function to extract the first POS
# def extract_first_pos(translation):
#     # parts = translation.split('.')
#     # first_part = parts[0].strip()
#     parts = translation.split(':')
#     pos = parts[0]
#
#     return pos.strip()
#
# # Apply the function to create a new column
# df['POS'] = df['GTPOSTRANS'].apply(extract_first_pos)
#



# df.to_csv(os.path.join('Frequency Lists',language,'Clean.csv'))