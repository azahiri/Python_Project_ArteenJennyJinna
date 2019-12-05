from flask import Flask, render_template, request

from run_analysis import *

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculate():
    if request.method == "POST":
        name = request.form["name"]
        gender = request.form['gender']
        name_value = value_of_name(name.lower())
        positive_words = create_list_from_file('positive-words.txt')
        word_list = find_positive_words_same_value(name.lower(), positive_words)

        year = highest_year(name, gender)
        print(year)

        if word_list:
            return render_template(
                "result.html", name=name, word_list=word_list, year=year, name_value=name_value
            )
        else:
            return render_template("index.html", error=True)
    return render_template("index.html", error=None)
