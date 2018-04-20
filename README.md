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

In config.yaml:

~~~yaml
Twitter:
  consumer_key:
  consumer_secret:
  access_token:
  access_token_secret:
  # replace "-weather-" to emoji, so insert "-weather-" to your name
  name: xx-weather-xx
OpenWeatherMap:
  cityid:
  appid:
Schedule:
  method: interval
  unit: minutes
  time: 1
~~~

# Docker

~~~
docker pull ckyol/twitter-weather-name

docker run --name twitter-name -v /etc/config.yaml:/usr/src/app/config.yaml -d ckyol/twitter-weather-name
~~~

