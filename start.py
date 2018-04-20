from apscheduler.schedulers.blocking import BlockingScheduler
from twitter_name import update_twitter_name
import time
import yaml

# Load config
config_file = open('config.yaml')
config = yaml.load(config_file)

# Twitter
consumer_key = config['Twitter']['consumer_key']
consumer_secret = config['Twitter']['consumer_secret']
access_token = config['Twitter']['access_token']
access_token_secret = config['Twitter']['access_token_secret']
name = config['Twitter']['name']
# OpenWeatherMap
cityid = config['OpenWeatherMap']['cityid']
appid = config['OpenWeatherMap']['appid']
# Schedule
method = config['Schedule']['method']
unit = config['Schedule']['unit']
times = config['Schedule']['time']

def job():
    """
    Scheduler job
    print your twitter name and time
    :return:
    """

    data = update_twitter_name(consumer_key,consumer_secret,
                        access_token,access_token_secret,
                        cityid,appid,
                        name)

    print(data.name)
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) )

scheduler = BlockingScheduler()
if method == 'interval':
    if unit == 'seconds':
        scheduler.add_job(job, 'interval', seconds=times)
    elif unit == 'minutes':
        scheduler.add_job(job, 'interval', minutes=times)
    elif unit == 'hours':
        scheduler.add_job(job, 'interval', hours=times)

scheduler.start()