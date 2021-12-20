import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def main():
    if request.method == "GET":
        return render_template('homepage.html')


@app.route('/flashcards', methods=['GET', 'POST'])
def flashcards():
    return render_template("flashcards.html")


if __name__ == "__main__":
    app.run(debug=False, port=8080, host='0.0.0.0')
