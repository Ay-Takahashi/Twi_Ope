from flask import Flask, render_template, request
from common.tweet import tweet_run

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    tweet_body = ""
    return render_template('index.html', tweet_body=tweet_body)


@app.route('/post', methods=["POST"])
def home():
    if request.method == 'POST':
        tweet_body = request.form.get('tweet_body')
        tweet_run(tweet_body)
        return render_template('tweet_complete.html', tweet_body=tweet_body)


@app.route('/complete')
def tweet_complete():
    return render_template('tweet_complete.html')


if __name__ == '__main__':
    app.run(debug=True)
