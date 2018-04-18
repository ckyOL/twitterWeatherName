import tweepy
from weather import get_weather,weather_emoji

def update_twitter_name(consumer_key,consumer_secret,
                        access_token,access_token_secret,
                        cityid,appid,
                        name):
    '''
    Update your Twitter name

    :param consumer_key: Twitter app consumer key
    :param consumer_secret: Twitter app consumer secret
    :param access_token: Twitter app access token
    :param access_token_secret: Twitter app access token secret
    :param cityid: Your city ID
    :param appid: Your OpenWeatherMap API key
    :param name: Your Twitter name (replace "-weather-" to emoji)
    :return:
    '''

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    weather_data = get_weather(cityid,appid)
    emoji = weather_emoji(weather_data)

    twitter_name = name.replace("-weather-",emoji)

    return api.update_profile(name=twitter_name)
