import requests

def get_weather(cityid,appid):
    '''
    Get weather data from OpenWeatherMap
    :param cityid: Your city ID
    :param appid: Your OpenWeatherMap API key
    :return: Weather data(weather icon name)
    '''
    payload = {'id': cityid, 'APPID': appid}
    data = requests.get('http://api.openweathermap.org/data/2.5/weather', params=payload)

    weather_data = data.json()
    weather_data = weather_data['weather'][0]
    weather_data = weather_data['icon']

    return weather_data

def weather_emoji(weather):
    '''
    Transfer weather data to emoji
    :param weather: Weather data(weather icon name)
    :return: Weather emoji
    '''

    # Weather icons code
    # https://openweathermap.org/weather-conditions
    emoji_case = {
        '01d': '☀️',
        '01n': '🌝',
        '02d': '⛅️',
        '02n': '⛅️',
        '03d': '🌥',
        '03n': '🌥',
        '04d': '☁️',
        '04n': '☁️',
        '09d': '🌦',
        '09n': '🌦',
        '10d': '🌧',
        '10n': '🌧',
        '11d': '⛈',
        '11n': '⛈',
        '13d': '❄️',
        '13n': '❄️',
        '50d': '🌫',
        '50n': '🌫',
    }

    return emoji_case.get(weather)


