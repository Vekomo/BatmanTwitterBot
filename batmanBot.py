#!/usr/bin/env python

import markovify
import tweepy
import ConfigParser
import time

#Get tokens from local file so nobody can just see it on gitHub and mess it up
config = ConfigParser.ConfigParser()
config.read('PATH TO CONFIG')

#Authorize for tweepy api
CONSUMER_KEY = config.get('TWITTER','CONSUMER_KEY')
CONSUMER_SECRET = config.get('TWITTER','CONSUMER_SECRET')
ACCESS_TOKEN = config.get('TWITTER','ACCESS_TOKEN')
ACCESS_SECRET = config.get('TWITTER','ACCESS_SECRET')
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)



# Get raw text as string.
with open('CONFIG') as f:
    text = f.read()

# Build the model.
text_model = markovify.Text(text)

#making a quick sentence


#Good tweet size, then tweet
while True:
    #perfect tweet size, 140. I know 280 is the limit, but c'mon...140 is just elegant
    sentence = text_model.make_short_sentence(140)
    api.update_status(status=sentence)
    print ("Tweeted: " + sentence)
    #Wait 1.5 hours before tweeting again
    time.sleep(5400)
