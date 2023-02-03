import pandas as pd
from googletrans import Translator

def addtranslation(rawcsv, lang = 'es'):
    df = pd.read_csv(rawcsv, sep="\t")
    df['occurrences (ppm)'].sum() + 150
    df['CUMSUM'] = df['occurrences (ppm)'].cumsum()
    df['CUMSUM']= round(df['CUMSUM']/10000)
    translator = Translator()
    df['GTInfo'] = df['word'].apply(lambda x: translator.translate(x ,src = lang, dest = 'en'))
    # df.to_csv('SpanishGoogle')

    translations = []
    for i in df['GTInfo']:
        difftranslations = []
        if i.extra_data['all-translations']:
            alltrans = ""
            for j in i.extra_data['all-translations']:
                alltrans += j[0]
                alltrans += ': '
                alltrans += ", ".join(j[1][:3])
                alltrans += '.  '
            translations.append(alltrans)
        else:
            translations.append(i.text)
    df['translation'] = translations

    return df

df = addtranslation('Spanish/SpanishRawWiki.txt', 'es')
df.to_csv('Spanish/SpanishGoogleQuizlet')


subdf = df[:2000]
quizlet = subdf[['word', 'translation']]
quizlet.to_csv('Spanish/Spanish0-2000.csv')

subdf = df[4000:]
quizlet = subdf[['word', 'translation']]
quizlet.to_csv('Spanish/Spanish4000-6000.csv')