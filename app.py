import pandas as pd
from flask import Flask, render_template, request
from character_scraping import character_scraping

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
    df_chinese = df['Chinese']
    df_pinyin = df['Pinyin']
    df_Role = df['Role']
    df_english = df['English']
    return render_template("translation.html", flashcards_chinese=df_chinese[0], pinyin=df_pinyin[0],
                           flashcards_english=df_english[0])


if __name__ == "__main__":
    app.run(debug=False, port=8080, host='0.0.0.0')
