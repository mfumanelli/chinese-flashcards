import pandas as pd
from flask import Flask, render_template, request
from character_scraping import character_scraping
import random

app = Flask(__name__)

df = character_scraping()


@app.route('/', methods=["GET", "POST"])
def main():
    if request.method == "GET":
        return render_template('homepage.html')


@app.route('/flashcards', methods=['GET', 'POST'])
def flashcards():
    global df
    while df.shape[0] > 0:
        if request.method == "GET":
            print(f'Number of words left: {df.shape[0]}')
            random_i = df.sample(1).index[0]
            #print(request.args.get('translate'))

            df_chinese = df['Chinese'][random_i]
            df_pinyin = df['Pinyin'][random_i]
            df_english = df['English'][random_i]

            if request.args.get('down') == "I didn't know this word! (T︿T)":
                df = df.copy()

            else:
                df = df.drop(random_i)

            if df.shape[0] == 0:
                return render_template("endpage.html")

            return render_template("flashcards.html", flashcards_chinese=df_chinese,
                               pinyin=df_pinyin,
                               flashcards_english=df_english)

if __name__ == "__main__":
    app.run(debug=False, port=8080, host='0.0.0.0')
