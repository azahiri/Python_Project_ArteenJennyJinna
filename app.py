#import all the necessary packages 
from flask import Flask, render_template, request
import os
import tweepy 
from textblob import TextBlob
import datetime
import matplotlib.pyplot as plt 

#import all the necessary functions from overall.py file 
from overall import remove_url, create_dictionary, clean_tweets, get_sentiment, get_label, auth, bar_plot

#setting the image folder for the barplot to be stored in 
image_folder = os.path.join('static', 'image')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = image_folder

@app.route("/", methods=["GET", "POST"])


def overall_sentiment_analysis():
    if request.method == "POST":
        api = auth()
        user_input = request.form["firstkeyword"]
        public_tweets = api.search(user_input, count = 1000)
        dictionary_tweets = create_dictionary(public_tweets)
        cleaned_tweets = clean_tweets(dictionary_tweets)
        polarity1 = get_sentiment(cleaned_tweets)[0]
        subjectivity1 = get_sentiment(cleaned_tweets)[1]
        analysis = get_sentiment(cleaned_tweets)
        label1 = get_label(analysis, threshold=0)

        #creating a if statement in case the user wants to analyze another keyword
        if  request.form['option'] == "yes":
            user_input2 = request.form["secondkeyword"]
            public_tweets2 = api.search(user_input2, count = 1000)
            dictionary_tweets2 = create_dictionary(public_tweets2)
            cleaned_tweets2 = clean_tweets(dictionary_tweets2)
            analysis2 = get_sentiment(cleaned_tweets2)
            polarity2 = get_sentiment(cleaned_tweets2)[0]
            subjectivity2 = get_sentiment(cleaned_tweets2)[1]
            label2 = get_label(analysis2, threshold=0)
            bar_plot(polarity1, subjectivity1, polarity2, subjectivity2, user_input, user_input2)
            full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'barplot.png')
            return render_template(
                "results1.htm", firstkeyword = user_input, polarity1 = polarity1, subjectivity1 = subjectivity1,
                label1= label1, secondkeyword = user_input2 , polarity2 = polarity2, subjectivity2 = subjectivity2,
                label2 = label2, barplot = full_filename) 

        else: 
            return render_template(
            "results2.htm", firstkeyword = user_input, polarity1 = polarity1, subjectivity1 = subjectivity1,
            analysis = analysis, label1=label1) 

    return render_template("overall.htm", error=None)

def home():
    return render_template("homepage.html")

if __name__ =='__main__':
    app1.run()