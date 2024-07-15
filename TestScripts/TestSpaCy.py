import pandas as pd
import spacy

df = pd.read_csv('../Frequency Lists/Spanish/Clean.csv').iloc[:100, :]
# Load the Spanish spaCy model
nlp = spacy.load("es_core_news_sm")

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

# Function to get POS, tag, and layman's description
def get_pos_tag_layman(word):
    doc = nlp(word)
    pos, tag, layman_description = None, None, None
    for token in doc:
        pos = token.pos_
        tag = token.tag_
        layman_description = pos_mapping.get(pos, 'Unknown')
    return pos, tag, layman_description

# Apply the function to each word in the DataFrame
df[['SpaCy_POS', 'SpaCy_Tag', 'POS']] = df['Spanish'].apply(lambda word: pd.Series(get_pos_tag_layman(word)))



# # Template sentences for different POS contexts
# templates = [
#     "Voy a [WORD].",  # Verb context
#     "El [WORD] está cerrado.",  # Noun context (masculine)
#     "La [WORD] está rota.",  # Noun context (feminine)
#     "Ella es muy [WORD].",  # Adjective context
#
#     # "¿Dónde está el [WORD]?",  # Noun context (location)
#     "El [WORD] rápido.",  # Adjective context (fast)
#     # "Yo [WORD] todos los días.",  # Verb context (daily action)
#     # "Es un [WORD] importante.",  # Noun context (important thing)
#     # "El [WORD] es alto.",  # Noun context (description)
#     # "Ella [WORD] cuando puede."  # Verb context (conditional action)
# ]
#
# # Function to generate sentences for a word
# def generate_sentences(word, templates):
#     sentences = []
#     for template in templates:
#         sentences.append(template.replace("[WORD]", word))
#     return sentences
#
# # Function to get POS tags for a word
# def get_pos_tags(word, templates):
#     pos_tags = set()
#     sentences = generate_sentences(word, templates)
#     for sentence in sentences:
#         doc = nlp(sentence)
#         for token in doc:
#             if token.text.lower() == word:
#                 pos_tags.add(token.pos_)
#     return list(pos_tags)
#
# # POS tag mapping to descriptions
# pos_map = {
#     "ADJ": "adjective",
#     "ADP": "adposition",
#     "ADV": "adverb",
#     "AUX": "auxiliary",
#     "CONJ": "conjunction",
#     "CCONJ": "coordinating conjunction",
#     "DET": "determiner",
#     "INTJ": "interjection",
#     "NOUN": "noun",
#     "NUM": "numeral",
#     "PART": "particle",
#     "PRON": "pronoun",
#     "PROPN": "proper noun",
#     "PUNCT": "punctuation",
#     "SCONJ": "subordinating conjunction",
#     "SYM": "symbol",
#     "VERB": "verb",
#     "X": "other",
#     "SPACE": "space"
# }
#
# # Simplified common POS mapping
# common_pos_map = {
#     "ADJ": "adjective",
#     "ADP": "preposition",
#     "ADV": "adverb",
#     "AUX": "auxiliary verb",
#     "CCONJ": "conjunction",
#     "DET": "determiner",
#     "INTJ": "interjection",
#     "NOUN": "noun",
#     "NUM": "numeral",
#     "PART": "particle",
#     "PRON": "pronoun",
#     "PROPN": "proper noun",
#     "SCONJ": "conjunction",
#     "SYM": "symbol",
#     "VERB": "verb",
#     "X": "other",
#     "PUNCT": "punctuation",
#     "SPACE": "space",
#     "CONJ": "conjunction"
# }
#
# # Function to map POS tags to their descriptions
# def map_pos_tags(pos_tags):
#     return [pos_map.get(tag, "unknown") for tag in pos_tags]
#
# # Function to map POS tags to common parts of speech
# def map_common_pos(pos_tags):
#     return [common_pos_map.get(tag, "unknown") for tag in pos_tags]
#
# # Apply the function to each word in the DataFrame
# df['spaCy_POS'] = df['lemma'].apply(lambda x: get_pos_tags(x, templates))
# df['POS'] = df['spaCy_POS'].apply(lambda x: map_pos_tags(x))
# df['Common_POS'] = df['spaCy_POS'].apply(lambda x: map_common_pos(x))
#
# # Save the updated DataFrame to a new CSV file
# df.to_csv("updated_dataframe.csv", index=False)
#
# # Display the updated DataFrame
# print(df)