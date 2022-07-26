import pandas as pd
from googletrans import Translator

df = pd.read_csv('Spanish', sep="\t")
df['occurrences (ppm)'].sum() + 150
df['CUMSUM'] = df['occurrences (ppm)'].cumsum()
df['CUMSUM']= round(df['CUMSUM']/10000)
translator = Translator()
df['GTInfo'] = df['word'].apply(lambda x: translator.translate(x ,src = 'es', dest = 'en'))
df.to_csv('SpanishGoogle')

quizlet = subdf[['word', 'English']]
quizlet.to_csv('Spanish2000-4000.csv')