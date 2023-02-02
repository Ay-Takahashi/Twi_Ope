import tweepy
from settings import CONFIG


def tweet_run(message):
    API_KEY = CONFIG["API_KEY"]
    API_SECRET = CONFIG["API_SECRET"]
    ACCESS_TOKEN = CONFIG["ACCESS_TOKEN"]
    ACCESS_TOKEN_SECRET = CONFIG["ACCESS_TOKEN_SECRET"]

    client = tweepy.Client(
        consumer_key=API_KEY,
        consumer_secret=API_SECRET,
        access_token=ACCESS_TOKEN,
        access_token_secret=ACCESS_TOKEN_SECRET,
    )

    # ツイート送信
    client.create_tweet(text=message)
