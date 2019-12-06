from flask import Flask, render_template, request
from overall import remove_url, create_dictionary, clean_tweets, get_sentiment, get_label, auth
import os
import tweepy 
from textblob import TextBlob
import datetime
import matplotlib.pyplot as plt 

image_folder = os.path.join('static', 'image')

app1 = Flask(__name__)
app1.config['upload_folder'] = image_folder

@app1.route("/", methods=["GET", "POST"])
@app1.route('/index')

def calculate():
    if request.method == "POST":
        api = auth()
        user_input = request.form["firstkeyword"]
        public_tweets = api.search(user_input, count = 1000)
        dictionary_tweets = create_dictionary(public_tweets)
        cleaned_tweets = clean_tweets(dictionary_tweets)
        polarity1 = get_sentiment(cleaned_tweets)[0]
        subjectivity1= get_sentiment(cleaned_tweets)[1]
        analysis = get_sentiment(cleaned_tweets)
        label1 = get_label(analysis, threshold=0)
    
        if  request.form['name'].value == "yes":
            user_input2 = request.form["secondkeyword"]
            public_tweets2 = api.search(user_input2, count = 1000)
            dictionary_tweets2 = create_dictionary(public_tweets2)
            cleaned_tweets2 = clean_tweets(dictionary_tweets2)
            analysis2 = get_sentiment(cleaned_tweets2)
            polarity2 = get_sentiment(cleaned_tweets2)[0]
            subjectivity2 = get_sentiment(cleaned_tweets2)[1]
            label2 = get_label(analysis2, threshold=0)
            full_filename = os.path.join(app.config['upload_folder'], 'barplot.png')
            return render_template(
                "results1.htm", firstkeyword = user_input, polarity = polarity1, subjectivty = subjectivity1,
                analysis = analysis, label1= label1, secondkeyword = user_input2 , polarity2 = polarity2, subjectivty2 = subjectivity2,
                label2 = label2, barplot = full_filename ) 

        else: 
            return render_template(
                "results1.htm", firstkeyword = user_input, polarity = polarity1, subjectivty = subjectivity1,
                analysis = analysis) 

    return render_template("overall.htm", error=None)

if __name__ =='__main__':
    app1.run()