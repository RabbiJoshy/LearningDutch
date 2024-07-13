import pandas as pd
import random
df = pd.read_csv('Dutch/Verbs/PastTenseVerbs.txt', sep = ' ')
list(df['Infinitive'])
translations = ['Be', 'Have', 'Should', 'Can', 'Go', 'Do', 'Know', 'Become', 'Say', 'Want', 'Will', 'Come', ' Sit', 'Make', 'Stand', 'See', 'Look', 'May', 'Let', 'Think', 'Get', 'Find', 'Live', 'Ask', 'Give' , 'Work', 'Read', 'Stay', 'Exist', 'Lying', 'Appear', 'Keep', 'Cost', 'Believe', 'Take', 'Eat', 'Appear', ' Start', 'Drink', 'Talk', 'Put', 'Walk', 'Fetch', 'Play', 'Fall', 'Happen', 'Concern', 'Hear', 'Know', 'Bring' , 'Learn', 'Imagine', 'Speak', 'Tell', 'Sleep', 'Couple', 'Grow', 'Use', 'Expect', 'Mean', 'Pay', 'Shape', ' Buy', 'Count', 'Concern', 'Bid', 'Sell', 'Follow', 'Draw', 'Determine', 'Search', 'Lay', 'Write', 'Limit', 'Money' , 'Lead', 'Amount', 'Wait', 'Place', 'Plan', 'Start', 'Try', 'Feed', 'Build', 'Choose', 'Provide', 'Involve', ' Help', 'Visit', 'Deliver', 'Reply', 'Call', 'Name', 'Change', 'Trust', ' Originate', 'Rise', 'Own', 'Feel']
df['English'] = translations
df['PastPerfectauxiliary'].astype(str)

listofdicts = dict()
for i, row in df.iterrows():
    vd = dict()
    listofdicts[row[0]] = {'Sing':row[1], 'Plural':row[2], 'Participle':row[4], 'Aux': row[3], 'eng': row[5], 'Infinitive': row[0] }

Eng = []
Dutch = []

PerfFront = []
PerfBack = []

for key in listofdicts.keys():
    print(key)
    vd = listofdicts[key]
    for i in ['Sing', 'Plural','Participle']:
        if i == 'Participle':
            if vd['Aux'] == 'is':
                Aux = random.choice([('Hij', 'is'), ('Jij', 'bent'), ('Ik', 'ben') ,('Zij', 'zijn')])
            elif vd['Aux'] == 'heeft':
                Aux = random.choice([('Hij', 'heeft'), ('Jij', 'hebt'), ('Ik', 'heb'), ('Zij', 'hebben')])

            PerfFront.append(Aux[0] + ' (' + vd['Aux'].lower() + ') ' + ': *' + vd['Infinitive'] + '*')
            PerfBack.append("{} {} {}".format(Aux[0], Aux[1], vd[i]))

        elif i == 'Sing':
            # Eng.append(random.choice(['Hij', 'Jij', 'Ik']) + ': *' + vd['Infinitive'] + '*')
            Eng.append("{}: *{}*".format(random.choice(['Hij', 'Jij', 'Ik']), vd['Infinitive']) )
            Dutch.append(vd[i])
        elif i == 'Plural':
            Eng.append("{}: *{}*".format(random.choice(['Wij', 'Jullie', 'Zij']), vd['Infinitive']))
            # Eng.append(random.choice(['Wij', 'Jullie', 'Zij']) + ': *' + vd['Infinitive'] + '*')
            Dutch.append(vd[i])

quizletsimple = pd.DataFrame()
quizletperfect = pd.DataFrame()
quizletsimple['SimpleFront'] = Eng
quizletsimple['SimpleBack'] = Dutch
quizletperfect['PerfFront'] = PerfFront
quizletperfect['PerfBack'] = PerfBack


quizletsimple.to_csv('Dutch/Verbs/Simple Past Tense.csv')
quizletperfect.to_csv('Dutch/Verbs/Perfect Past Tense.csv')

import pandas as pd
df = pd.read_csv('Past Tense.csv')
print(listofdicts)