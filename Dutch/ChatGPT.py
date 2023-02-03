import pandas as pd
import math
import os
from chatgpt_wrapper import ChatGPT
import openai
# bot = ChatGPT()
language = 'Dutch'
openai.api_key = "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"
model_engine = 'text-davinci-003'
sets = os.listdir('Dutch/Vocabulary/Split_Sets/')
subsets = ['100-200.csv','200-300.csv','300-400.csv', '400-500.csv', '600-700.csv', '700-800.csv', '500-600.csv']

def firstpass(extension, language = 'Dutch', model_engine = 'text-davinci-003'):

    df = pd.read_csv(language + '/Vocabulary/Split_Sets/' + extension)
    responses = []
    for i, row in df.iterrows():
        print(i)
        print(row[language])
        print("write a sentence in dutch using the word " + row[language] + " with an english translation")
        prompt = "write a sentence in dutch using the word " + row[language] + " with an english translation"
        completion = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
        response = completion.choices[0].text
        print(response)
        responses.append(response)
    df['Sentence'] = responses
    df.to_csv(language +'/Vocabulary/ChatGPT_Sets/' + extension)

    return df

for set in subsets:
    firstpass(set, 'Dutch', model_engine)
view = pd.read_csv('Dutch/Vocabulary/ChatGPT_Sets/0-100.csv')



# df100 = pd.read_csv('Dutch/Vocabulary/ChatGPT_Sets/100-200.csv')
# responses = []
# for i, row in df100.iterrows():
#     if row['Sentence'][:26] == 'Unusable response produced':
#         print(row['Dutch'])
#         print(row['Sentence'])
#         response = bot.ask("write a sentence in dutch using the word " + row['Dutch'] + " with an english translation")
#         print('asking')
#         print(response)
#         if response[:26] == 'Unusable response produced':
#             break
#         df100['Sentence'][i] = response
#         print('saving')
#         df100.to_csv('Dutch/Vocabulary/ChatGPT_Sets/0-100.csv')
#         responses.append((i,response))
#         print(responses)

word = 'bent'
print("write a sentence in dutch using the word " + word + " with an english translation")
prompt = "write a sentence in dutch using the word " + word + " with an english translation"
# completion = openai.Completion.create(
#     engine= 'text-davinci-003',
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)
print(completion.choices[0].text)







# df100 = pd.read_csv('Dutch/Vocabulary/ChatGPT_Sets/0-100.csv')
# responses = []
# for i, row in df100.iterrows():
#     if row['Sentence'][:26] == 'Unusable response produced':
#         print(row['Dutch'])
#         print(row['Sentence'])
#         response = bot.ask("write a sentence in dutch using the word " + row['Dutch'] + " with an english translation")
#         print('asking')
#         print(response)
#         if response[:26] == 'Unusable response produced':
#             break
#         df100['Sentence'][i] = response
#         print('saving')
#         df100.to_csv('Dutch/Vocabulary/ChatGPT_Sets/0-100.csv')
#         responses.append((i,response))
#         print(responses)



# bot.ask('Hello')