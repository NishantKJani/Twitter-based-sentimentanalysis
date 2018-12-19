import nltk
nltk.download('punkt')
from textblob import TextBlob

wiki=TextBlob("Nishant Jani is the most dangerous person ever met")
print(wiki.tags)
print(wiki.words)
print(wiki.sentiment.polarity)




import tweepy
from textblob import TextBlob

consumer_key="YOUR-CONSUMER-KEY"
consumer_secret="YOUR-CONSUMER-SECRET-KEY"

access_token="YOUR-ACCESS-TOKEN-KEY"
access_token_secret="YOUR-ACCESS-TOKEN-SECRET-KEY"

auth=tweepy.OAuthHandler(consumer_key,consumer_secret)

auth.set_access_token(access_token,access_token_secret)

api=tweepy.API(auth)

public_tweets=api.search('Trump')

for a in public_tweets:
    print(a.text)
    analysis=TextBlob(a.text)
    print(analysis.sentiment)
    print()
