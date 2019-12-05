#import necessary libraries 
import tweepy 
from textblob import TextBlob
import datetime
import re
import pandas as pd
##Functions to Validate and Clean 

# function to remove url! 
def remove_url(txt): 
    return " ".join(re.sub("([^0-9A-Za-z \t])|(\w+:\/\/\S+)", "", txt).split())

#Date input validation
def validate(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Incorrect data format, should be YYYY-MM-DD")



#authenticate the keys 
consumer_key = 'WWSMyFjVOJzjR5wtXizC1B0go'
consumer_secret = 'w1DsVNTFc4v9fdtSItr3V8O2JVsleSHlvhdkhckoSit6AKP9XP'
access_token = '1115278543863386112-aqOKS4yOFao6ZUe6PaQwWxYOJyk3gP' 
acccess_token_secret = 'HKHbROYbNNxP50GsluZ1wf4h6GjAhSKh6j69GOWGFnilW' 

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, acccess_token_secret)
api = tweepy.API(auth)

# #Step 1- validate date 
# since_date = validate(input('Enter starting date in the form of  (YYYY-MM-DD): '))
# until_date = validate(input('Enter ending date in the form of (YYYY-MM-DD): '))

# # Step 3 - Retrieve Tweets
# user_input = input('Which topic would you like to search for on Twitter: ')
# public_tweets = api.search(user_input, count = 100, since = since_date , until=until_date)
search = input(str("What search term do you want to search? "))
public_tweets=api.search(search)


# print(public_tweets)
def create_dictionary(public_tweets):
    """
    
    """
    tweet_dictionary={}
    for tweet in public_tweets:
        # print(dir(tweet))
        # print(tweet.text, tweet.id)
        # print(dir(tweet.user))
        # print(tweet.user.screen_name)
        key = tweet.user.screen_name
        if key not in tweet_dictionary:
            tweet_dictionary[key] = [tweet.text]
        else: 
            tweet_dictionary[key].append(tweet.text)
    return tweet_dictionary

# print(create_dictionary(public_tweets))

dictionary_tweets = create_dictionary(public_tweets)



# tweets = api.user_timeline('realDonaldTrump')
# print(dir(tweets[0]))
# print(tweets[0].text)
# print(tweets[0].id, tweets[0].text, tweets[0].created_at)

# to print tweets
# CLEANS LIST OF DICTIONARY
def clean_tweets(dictionary_tweets):
    for key, value in dictionary_tweets.items():
        count = 0
        for word in value:
            # print(words)
            # print(type(words))
            word = re.sub('@[^\s]+','',word) #gets rid of id 
            word = remove_url(word) #gets rid of url
            word = word.strip('RT') #get rid of rt
            dictionary_tweets[key][count] = word
            count += 1
    # print(dictionary_tweets)
    return dictionary_tweets

cleaned_tweets = clean_tweets(dictionary_tweets)
# print(cleaned_tweets)
# print({key:value for key, value in cleaned_tweets.items() if len(value) > 1}) 
#^ to check if there's more than one value



## Create dictionary of twitter per ID
# def create_dictionary(cleaned_tweets):
#     d = dict()
#     for tweets in cleaned_tweets:
#         key =



# Get sentiment analysis 
def get_sentiment(cleaned_tweets):
    total_polarity = 0
    total_subjectivity = 0
    num_tweets = 0
    for value in cleaned_tweets.values(): 
        for tweet in value:
            text = TextBlob(tweet)
            total_polarity += text.sentiment.polarity
            total_subjectivity += text.sentiment.subjectivity
            num_tweets += 1
    avg_polarity = total_polarity / num_tweets
    avg_subjectivity = total_subjectivity / num_tweets
    return avg_polarity, avg_subjectivity



print(f"Polarity: {get_sentiment(cleaned_tweets)[0]:.3f}", f"Subjectivity: {get_sentiment(cleaned_tweets)[1]:.3f}")
# sentiment = get_sentiment(dictionary_tweets)
# where polarity is a float within the range [-1.0, 1.0] 
# and subjectivity is a float within the range [0.0, 1.0] where 0.0 is very objective and 1.0 is very subjective.


# # def sentiment_analysis(tweets_final)': 
# # for tweet in cleaned_tweets: 
# #     analysis= textblob(tweet.cleaned_tweets)
# #     return analysis


# write a function that tells us if the tweet is positive or not 
# def get_label(analysis, threshold=0): # threshold
#     if analysis.sentiment[0] > threshold:
#        return 'Positive'
#     else:
#         return 'Negative'


sentiment_df = pd.DataFrame(cleaned_tweets)

sentiment_df.head()

print(sentiment_df)

