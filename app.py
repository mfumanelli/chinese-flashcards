import pandas as pd
from flask import Flask, render_template, request
from character_scraping import character_scraping
import random

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def main():
    if request.method == "GET":
        return render_template('homepage.html')


@app.route('/flashcards', methods=['GET', 'POST'])
def flashcards():
    df = character_scraping()
    df_chinese = df['Chinese']
    df_pinyin = df['Pinyin']
    df_Role = df['Role']
    df_english = df['English']
    return render_template("flashcards.html", flashcards_chinese=df_chinese[0], pinyin=df_pinyin[0],
                           flashcards_english=df_english[0])


@app.route('/flashcards-translation', methods=['GET', 'POST'])
def translation():
    df = character_scraping()
    while df.shape[0] > 0:
        print(df.shape[0])
        random_i = random.randint(0, df.shape[0])
        if request.method == "GET":
            if request.args.get('up') is None:
                df = df.copy()
                action = render_template("translation.html", flashcards_chinese=df['Chinese'][random_i],
                                       pinyin=df['Pinyin'][random_i],
                                       flashcards_english=df['English'][random_i])
            else:
                action = render_template("translation.html", flashcards_chinese=df['Chinese'][random_i],
                                           pinyin=df['Pinyin'][random_i],
                                           flashcards_english=df['English'][random_i])
                df = df.drop(random_i)
            return action

def contact():
    if request.method == 'POST':
        if request.form['submit_button'] == 'Do Something':
            pass  # do something
        elif request.form['submit_button'] == 'Do Something Else':
            pass  # do something else
        else:
            pass  # unknown
    elif request.method == 'GET':
        return render_template('contact.html', form=form)


if __name__ == "__main__":
    app.run(debug=False, port=8080, host='0.0.0.0')
