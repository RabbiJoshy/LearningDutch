import pandas as pd
import re
import os
language = 'Spanish'
def clean(file_path = os.path.join('Frequency Lists',language,'Raw.txt')):
    df = pd.read_csv(file_path, sep = '\t')
    df['occurrences (ppm)'].sum() + 150
    df['CUMSUM'] = df['occurrences (ppm)'].cumsum()
    df['CUMSUM']= round(df['CUMSUM']/10000)
    df['Number'] = df['rank']
    df['Spanish'] = df['word']
    df = df.rename(columns = {'lemma forms': 'lemma'})
    return df

df = clean()


def expand_lemma_forms(df):
    # Create a list to hold the new rows
    new_rows = []

    # Loop through each row in the DataFrame
    for index, row in df.iterrows():
        lemma_forms = row['lemma']

        # Check if lemma forms contain multiple words separated by a space
        if ' ' in lemma_forms:
            # Split the lemma forms into individual words
            parts = lemma_forms.split()
            # Create a new row for each part
            for part in parts:
                new_row = row.copy()
                new_row['lemma'] = part
                new_row['lemma (disambiguated)'] = part
                new_rows.append(new_row)
        else:
            # If there's only one word, keep the row as is
            new_rows.append(row)


    # Create a new DataFrame from the list of new rows
    new_df = pd.DataFrame(new_rows).reset_index(drop=True)

    # Generate the 'show' column as per the previous logic
    new_df['show'] = new_df.apply(
        lambda row: f"*{row['word']}* ({row['lemma']})" if row['lemma'] != row['word'] else row['word'],
        axis=1)

    return new_df
df = expand_lemma_forms(df)

df['show'] = df.apply(lambda row:
                      f"*{row['word']}* ({row['lemma']})" if row['lemma'] != row['word'] else row['word'], axis=1)
df[['rank', 'lemma', 'Spanish', 'lemma (disambiguated)', 'show']].to_csv(
    os.path.join('Frequency Lists',language,'Clean.csv'))