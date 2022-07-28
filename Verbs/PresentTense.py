import nltk
# nltk.download('omw-1.4')
import pandas as pd
from pattern.nl import conjugate, lemma, lexeme, tenses, PRESENT, FUTURE, PAST, SG, PL
# print(conjugate(verb='zijn',tense= 'present',person=1, mood = "indicative", aspect = "imperfective"))
# for infinitive in infinitives:
#     print(lexeme(infinitive))

# x = lexeme('be')
# from pattern.en import conjugate, lemma, lexeme, tenses, PRESENT, FUTURE, PAST, SG, PL
# print(conjugate(verb='be',tense= 'past',person=1, mood = "indicative", aspect = "perfective"))

df = pd.read_csv('Verbs/PastTenseVerbs.txt', sep = ' ')
translations = ['Be', 'Have', 'Should', 'Can', 'Go', 'Do', 'Know', 'Become', 'Say', 'Want', 'Will', 'Come', ' Sit',
                'Make', 'Stand', 'See', 'Look', 'May', 'Let', 'Think', 'Get', 'Find', 'Live', 'Ask', 'Give' , 'Work',
                'Read', 'Stay', 'Exist', 'Lying', 'Appear', 'Keep', 'Cost', 'Believe', 'Take', 'Eat', 'Appear', ' Start',
                'Drink', 'Talk', 'Put', 'Walk', 'Fetch', 'Play', 'Fall', 'Happen', 'Concern', 'Hear', 'Know', 'Bring' ,
                'Learn', 'Imagine', 'Speak', 'Tell', 'Sleep', 'Couple', 'Grow', 'Use', 'Expect', 'Mean', 'Pay', 'Shape',
                ' Buy', 'Count', 'Concern', 'Bid', 'Sell', 'Follow', 'Draw', 'Determine', 'Search', 'Lay', 'Write',
                'Limit', 'Money' , 'Lead', 'Amount', 'Wait', 'Place', 'Plan', 'Start', 'Try', 'Feed', 'Build', 'Choose',
                'Provide', 'Involve', ' Help', 'Visit', 'Deliver', 'Reply', 'Call', 'Name', 'Change', 'Trust',
                ' Originate', 'Rise', 'Own', 'Feel']
infinitives = list(df['Infinitive'])

listofdicts = dict()
for infinitive in infinitives:
    listofdicts[infinitive] = {'ik':conjugate(verb= infinitive, tense=PRESENT,number=SG, person = 1),
                               'zij':conjugate(verb= infinitive, tense=PRESENT,number=PL, person = 3),
                               'wij': conjugate(verb=infinitive, tense=PRESENT, number=PL, person=1),
                               'hij': conjugate(verb=infinitive, tense=PRESENT, number=SG, person=3),
                               'jij':conjugate(verb= infinitive, tense=PRESENT,number=SG, person = 2)}

conjtable = pd.DataFrame.from_dict(listofdicts).transpose()

front = []
altfront = []
back = []
for pronoun in conjtable.columns:
    for inf in infinitives:
        front.append(pronoun + ' : ' + inf)
        # altfront.append()
        back.append(conjtable.loc[inf, pronoun])
quizlet = pd.DataFrame()
quizlet['Front'] = front
# quizlet['Alternate'] = altfront
quizlet['Back'] = back

quizlet.to_csv('Verbs/Flashcards Present Tense')