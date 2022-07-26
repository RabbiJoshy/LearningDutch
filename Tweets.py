import tweepy
import pandas as pd
import json

def searchfortweet(keyword):
    API_KEY = 'F7Hlb9rJdFHgV1OgJuY9cIYzl'
    API_SECRET = 'QyxTmDdxlNMZ3Rj8N4eAmnb6bPny058P1kYuXuaGrmdqQSFfOf'
    ACCESS_TOKEN = '157478333-AMmAeBCXDDOk1AjWbT1p5jJHhW1mecOEBxX5tAZB'
    ACCESS_SECRET = 'D2eW7aNhGNwUHrTc03zEREtiO6K2Ya7InI4XZhdGOvx6T'
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=False)

    # filter = "-filter:retweets -filter:media -filter:links filter:verified -filter:replies"
    # filter = "-filter:replies"
    # filter = "-filter:links -filter:replies"
    language = 'nl'  # or 'es'
    keyword = 'ik'
    query = keyword #+ filter

    tweet_iterator = api.search_tweets(q=query, lang=language, count = 10, tweet_mode='extended')
    json_data = [r._json for r in tweet_iterator]
    df = pd.json_normalize(json_data)
    # df = df.loc[df['full_text'].str.len() < 280][['user.followers_count', 'full_text']]
    if len(df['full_text']) > 0:
        text = df['full_text'][0]
        textwords = text.split("\n")
        textwords = " ".join(textwords)
        textwords = textwords.split(" ")
        textsplit = [word for word in textwords if "@" not in word and '#' not in word and 'RT' not in word]
        texttweet = " ".join(textsplit)
    else:
        texttweet = 'no tweet found'

    return texttweet

x = pd.read_csv('Translated_Sets/0-200.csv')
words = x['Dutch']
tweets = []
for word in words:
    print(word)
    tweet = searchfortweet(word)
    tweets.append(tweet)
