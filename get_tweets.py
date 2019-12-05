# General:
import tweepy           # To consume Twitter's API
import pandas as pd     # To handle data
import numpy as np      # For number computing

# For plotting and visualization:
from IPython.display import display
import matplotlib.pyplot as plt
import seaborn as sns
'exec(%matplotlib inline)'
import time
import datetime
import pickle

# We import our access keys:
from credentials import *    # This will allow us to use the keys as variables

input_keywords = input("Enter a list keywords separated by comma: ")
KEYWORDS = input_keywords.split(',')
SCREEN_NAME = input('Screen Name: @')


# API's setup:
def twitter_setup():
    """
    Utility function to setup the Twitter's API
    with our access keys provided.
    """
    # Authentication and access using keys:
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    # Return API with authentication:
    api = tweepy.API(auth)
    return api

def get_tweets_by_username(screen_name):
    """We create an extractor object:"""
    extractor = twitter_setup()
    tweets = tweepy.Cursor(extractor.user_timeline, screen_name=screen_name)

    return tweets

tweets = get_tweets_by_username(screen_name=SCREEN_NAME)

tweet_list = list(tweets.items())

with open(f'tweets_by_{SCREEN_NAME}.p', 'wb') as f:
    pickle.dump(tweet_list, f)

# tweets = get_tweets_by_username(screen_name=SCREEN_NAME)

# # print(len(list(tweets.items())))
# tweet_list = list(tweets.items())
# with open(f'tweets_by_{SCREEN_NAME}.p', 'wb') as f:
#     pickle.dump(tweet_list, f)