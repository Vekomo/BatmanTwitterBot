import markovify
import tweepy
import ConfigParser
import time

#Get tokens from local file so nobody can just see it on gitHub and mess it up
config = ConfigParser.ConfigParser()
config.read('PATH TO CONFIG FILE')

#Authorize for tweepy api
CONSUMER_KEY = config.get('TWITTER','CONSUMER_KEY')
CONSUMER_SECRET = config.get('TWITTER','CONSUMER_SECRET')
ACCESS_TOKEN = config.get('TWITTER','ACCESS_TOKEN')
ACCESS_SECRET = config.get('TWITTER','ACCESS_SECRET')
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)




# Get raw text as string.
with open("PATH TO BATMAN TEXT FROM WIKIA") as f:
    text = f.read()

# Build the model.
text_model = markovify.Text(text)

#making a quick sentence
sentence = text_model.make_sentence()

#Good tweet size, then tweet
if len(sentence) <= 140:
    api.update_status(status=sentence)
    print sentence
