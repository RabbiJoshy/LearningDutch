import json
with open('../config.json') as config_file:
    config = json.load(config_file)
    YANDEX_API_KEY = config['Yandex_api_key']

import pandas as pd
import requests

df = pd.read_csv('../Frequency Lists/Spanish/Clean.csv').iloc[:20, :]
YANDEX_TRANSLATE_URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
YANDEX_DICTIONARY_URL = 'https://dictionary.yandex.net/api/v1/dicservice.json/lookup'

def get_translations(word, lang_from='es', lang_to='en'):
    params = {
        'key': YANDEX_API_KEY,
        'lang': f'{lang_from}-{lang_to}',
        'text': word
    }
    response = requests.get(YANDEX_DICTIONARY_URL, params=params)
    if response.status_code != 200:
        return None

    data = response.json()
    translations = []

    if 'def' in data:
        for entry in data['def']:
            for tr in entry['tr']:
                translation = tr['text']
                pos = tr.get('pos', 'unknown')
                freq = tr.get('fr', 'unknown')
                translations.append({'translation': translation, 'pos': pos, 'frequency': freq})

    return translations


# Apply function to each row in the 'Spanish' column
df['Translations'] = df['Spanish'].apply(lambda x: get_translations(x))
