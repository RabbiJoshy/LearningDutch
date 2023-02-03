import pandas as pd
import math
from googletrans import Translator
import os
from chatgpt_wrapper import ChatGPT
bot = ChatGPT()
freqfile = 'Dutch/Vocabulary/AllFrequencies.txt'
language = 'Dutch'
df = pd.read_csv(freqfile, sep=" ")

def split_into_studysets(df, splitsize = 100, language = 'Dutch'):
    frequencydf = df
    # frequencydf['Frequency'] = frequencydf['Frequency'].astype(int)
    # frequencydf['cumsum'] = frequencydf['Frequency'].cumsum()/(0.01 * frequencydf['Frequency'].sum())
    for i in range(math.floor(len(frequencydf)/splitsize)):
        subdf = frequencydf[splitsize*i: splitsize*(i+1)].reset_index()[[language]]
        subdf.to_csv(language +'/Vocabulary/Split_Sets/' + str(splitsize*i) + '-' + str(splitsize*(i+1)) + '.csv')
    remaindersubdf = frequencydf[-(len(frequencydf)%splitsize):].reset_index()[[language]]
    remaindersubdf.to_csv('Dutch/Vocabulary/Split_Sets/' + 'Remainder.csv')

    return subdf

ss = split_into_studysets(df)












def addtranslation(df, lang = 'nl', originalcolumn = 'Dutch'):
    total = df['Frequency'].sum()
    df['CUMSUM'] = df['Frequency'].cumsum()
    df['CUM%'] = df['CUMSUM']/(total/100)
    translator = Translator()
    df['GTInfo'] = df[originalcolumn].apply(lambda x: translator.translate(x ,src = lang, dest = 'en'))

    translations = []
    for i in df['GTInfo']:
        difftranslations = []
        if i.extra_data['all-translations']:
            alltrans = ""
            for j in i.extra_data['all-translations']:
                alltrans += j[0]
                alltrans += ': '
                alltrans += ", ".join(j[1][:2])
                alltrans += '.  '
            translations.append(alltrans)
        else:
            translations.append(i.text)
    df['translation'] = translations

    return df

def makequizletcsv(df, start = 0, end = len(df)):
    subdf = df[start:end]
    transdf = addtranslation(subdf,'nl', 'Dutch')

    return transdf

Translateddf = makequizletcsv(df)
Translateddf.to_csv("Dutch/FrequencyTranslated")