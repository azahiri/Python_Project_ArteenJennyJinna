#import necessary libraries 
import tweepy 
from textblob import TextBlob
import datetime
import re 
##Functions to Validate and Clean 

# function to remove url! 
# def remove_url(txt): 
#     return " ".join(re.sub("([^0-9A-Za-z \t])|(\w+:\/\/\S+)", "", txt).split())

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
public_tweets=api.search('trump')
print(public_tweets)
##to print tweets
# def clean_tweets(public_tweets):
#     cleaned_tweets=[]
#     for tweets in public_tweets:
#         tweets_no_id = re.sub('@[^\s]+','',tweets.text) #gets rid of id 
#         tweets_no_url = remove_url(public_tweets) #gets rud of url
#         tweets_no_rt = tweets_no_url.strip('RT') #get rid of rt 
#         cleaned_tweets.append(tweets_no_rt)
#     return cleaned_tweets


# cleaned_tweets= clean_tweets(public_tweets)
# print(cleaned_tweets)

## Get sentiment analysis 
# def get_sentiment(cleaned_tweets):
#     text_list=[]
#     for tweet in cleaned_tweets: 
#         text= TextBlob(tweet)
#         text_list.append(text)
#         polarity = text.sentiment.polarity
#         subjectivity = text.sentiment.subjectivity
#     print(f'polarity: {}'+ polarity)
#     print(f'subjectivity: {}' + subjectivity)

# print(get_sentiment(cleaned_tweets))


# def sentiment_analysis(tweets_final)': 
# for tweet in cleaned_tweets: 
#     analysis= textblob(tweet.cleaned_tweets)
#     return analysis


#write a function that tells us if the tweet is positive or not 
# def get_label(analysis, threshold=0): # threshold
#     if analysis.sentiment[0] > threshold:
#        return 'Positive'
#      else:
#         return 'Negative'


