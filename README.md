# twitter Weather Name

Update your twitter name with weather emoji ☀️ ⛅️ 🌥 ☁️ 🌦 🌧 ⛈ ❄️ 🌫 

# Inspire by

> Twitterの名前を5分毎に東京の天気☼☂☃と連動させるサーバレスプログラムを書いたら色々知らないことが出てきた話
> [https://qiita.com/issei_y/items/ab641746be2704db98be](https://qiita.com/issei_y/items/ab641746be2704db98be)

# Install 

~~~ python
pip install -r requirements.txt
~~~

# How to use

In start.py:

1.Twitter app and OpenWeatherMap API key 

~~~python
# Twitter
consumer_key=''
consumer_secret=''
access_token=''
access_token_secret=''
# OpenWeatherMap
appid=''
~~~

2.City ID and twitter name 

~~~python
# replace "-weather-" to emoji, so insert "-weather-" to your name
name=''
cityid=''
~~~

3.Schedule

~~~python
# Sample
# update twitter name every 10 minutes
scheduler.add_job(job, 'interval', seconds=10)
# at 12:00
scheduler.add_job(job, 'cron', day_of_week='1-7', hour=12, minute=00)
~~~ 

