import pandas as pd
import math
from googletrans import Translator
import os

def split_into_studysets(freqfile = "AllFrequencies.txt"):
    frequencydf = pd.read_csv(freqfile, sep=" ")
    frequencydf['Frequency'] = frequencydf['Frequency'].astype(int)
    frequencydf['cumsum'] = frequencydf['Frequency'].cumsum()/(0.01 * frequencydf['Frequency'].sum())
    for i in range(math.floor(len(frequencydf)/200)):
        subdf = frequencydf[200*i: 200*(i+1)].reset_index()
        subdf.to_csv('Frequencies/' + str(200*i) + '-' + str(200*(i+1)) + '.csv')
    remaindersubdf = frequencydf[-(len(frequencydf)%200):].reset_index()
    remaindersubdf.to_csv('Frequencies/' + 'Remainder')

    return subdf
ss = split_into_studysets()


def add_google_info(rawfreq_file):
    subdf = pd.read_csv(rawfreq_file)
    subdf.rename(columns={'Unnamed: 0': 'index'}, inplace=True)
    translator = Translator()
    GoogleTransPosInfo = []
    GoogleTransLemmaInfo = []
    GoogleEnglish = []
    for dutchword in subdf['Dutch']:
        print(dutchword)
        translation = translator.translate(dutchword ,src = 'nl', dest = 'en')
        all_translations = translation.extra_data['all-translations']
        if not all_translations is None:
            all_translations = all_translations[0]
            pos = all_translations[0]
            lemma = all_translations[3]
            eng = " ".join(all_translations[1][:3])
        else:
            pos = 'No Google Info'
            eng = 'No Google Info'
            lemma = 'No Google Info'
        GoogleTransPosInfo.append(pos)
        GoogleTransLemmaInfo.append(lemma)
        GoogleEnglish.append(eng)
    subdf['GooglePos'] = GoogleTransPosInfo
    subdf['GoogleLemma'] = GoogleTransLemmaInfo
    subdf['GoogleEnglish'] = GoogleEnglish

    return subdf
for rawfreqfile in os.listdir('Frequencies'):
    googleset = add_google_info('Frequencies/' + rawfreqfile)
    googleset.to_csv('Translated_Sets/' +rawfreqfile)

def make_set_quizlet_ready(gtfile):
    setdf = pd.read_csv(gtfile)
    setdf['Quizlet'] = setdf['GooglePos'] + ', ' + setdf['GoogleEnglish']
    quizletdf = setdf[['Dutch', 'Quizlet']]

    return quizletdf
for rawfreqfile in os.listdir('Translated_Sets'):
    if rawfreqfile != '.DS_Store':
        quizletset = make_set_quizlet_ready('Translated_Sets/' + rawfreqfile)
        quizletset.to_csv('QuizletReadySets/' + rawfreqfile)


setdf = pd.read_csv('Translated_Sets/1200-1400.csv')



from sklearn.preprocessing import StandardScaler
df[['cost', 'sales']] = StandardScaler().fit_transform(df[['cost', 'sales']])