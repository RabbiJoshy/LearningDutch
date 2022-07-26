import pandas as pd
import random
df = pd.read_csv('Verbs.txt', sep = ' ')
list(df['Infinitive'])
translations = ['Be', 'Have', 'Should', 'Can', 'Go', 'Do', 'Know', 'Become', 'Say', 'Want', 'Will', 'Come', ' Sit', 'Make', 'Stand', 'See', 'Look', 'May', 'Let', 'Think', 'Get', 'Find', 'Live', 'Ask', 'Give' , 'Work', 'Read', 'Stay', 'Exist', 'Lying', 'Appear', 'Keep', 'Cost', 'Believe', 'Take', 'Eat', 'Appear', ' Start', 'Drink', 'Talk', 'Put', 'Walk', 'Fetch', 'Play', 'Fall', 'Happen', 'Concern', 'Hear', 'Know', 'Bring' , 'Learn', 'Imagine', 'Speak', 'Tell', 'Sleep', 'Couple', 'Grow', 'Use', 'Expect', 'Mean', 'Pay', 'Shape', ' Buy', 'Count', 'Concern', 'Bid', 'Sell', 'Follow', 'Draw', 'Determine', 'Search', 'Lay', 'Write', 'Limit', 'Money' , 'Lead', 'Amount', 'Wait', 'Place', 'Plan', 'Start', 'Try', 'Feed', 'Build', 'Choose', 'Provide', 'Involve', ' Help', 'Visit', 'Deliver', 'Reply', 'Call', 'Name', 'Change', 'Trust', ' Originate', 'Rise', 'Own', 'Feel']
df['English'] = translations
df['PastPerfectauxiliary'].astype(str)

listofdicts = dict()
for i, row in df.iterrows():
    vd = dict()
    listofdicts[row[0]] = {'Sing':row[1], 'Plural':row[2], 'Participle':row[4], 'Aux': row[3], 'eng': row[5] }

Eng = []
Dutch = []
for key in listofdicts.keys():
    print(key)
    vd = listofdicts[key]
    for i in ['Sing', 'Plural','Participle']:
        if i == 'Participle':
            if vd['Aux'] != 'none':
                if vd['Aux'].lower() == 'is':
                    Eng.append(random.choice(['Hij']) + ' ' + vd['Aux'] + ': ' + ' ' + vd['eng'])
                    Dutch.append(vd['Aux'] + " " +vd[i])
                elif vd['Aux'] == 'heeft':
                    Eng.append(random.choice(['Hij']) + ' ' + vd['Aux'] + ': ' + ' ' + vd['eng'])
                    Dutch.append(vd['Aux'] + " " + vd[i])
        elif i == 'Sing':
            Eng.append(random.choice(['Hij', 'Jij', 'Ik']) + ': ' + vd['eng'])
            Dutch.append(vd[i])
        elif i == 'Plural':
            Eng.append(random.choice(['Wij', 'Jullie', 'Zij']) + ': ' + vd['eng'])
            Dutch.append(vd[i])

quizlet = pd.DataFrame()
quizlet['Front'] = Eng
quizlet['Back'] = Dutch

quizlet.to_csv('Past Tense.csv')

import pandas as pd
df = pd.read_csv('Past Tense.csv')