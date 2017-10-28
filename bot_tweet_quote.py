import requests  # Requests is a http library written for humans
import json  # JSON is a Python inbuilt library that makes it easy to work with json.
import tweepy  # Tweepy is a Twitter API wrapper
import time


# Visit apps.twitter.com to get the following variables
consumer_key = 'consumer_key'
consumer_secret = 'consumer_secret'
access_token = 'access_token'
access_token_secret = 'access_token_secret'


# Twitter requires oAuth2 to access its API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)  # This creates an object called api


# I used RapidAPI to get access to the Random Quotes Generator
api_key = 'api_key'
api_url = 'https://andruxnet-random-famous-quotes.p.mashape.com?cat=famous&count=1'


def get_quotes():
    """This function gets random quotes from an API'

    It makes use of RapidAPI to access the Random Quotes Generator
    :return: It returns a dictionary object
    """
    headers = {'X-Mashape-Key': api_key, 'X-Mashape-Host': api_url}
    response = requests.get(api_url, headers=headers)
    json_converted_dictionary = json.loads(response.content.decode())
    json_converted_dictionary = json_converted_dictionary['quote']+' --'+json_converted_dictionary['author']
    return json_converted_dictionary


def tweet_quote():
    """This function updates Twitter with quotes.

    It tweets quotes gotten from get_quotes() function.
    :return: It has no return value
    """
    for i in range(1, 10):
        quote = get_quotes()
        time.sleep(30)
        try:
            api.update_status(quote)  # This method is accessed in tweepy
            print('Done')
        except tweepy.error.TweepError:
            pass


if __name__ == '__main__':
    tweet_quote()
