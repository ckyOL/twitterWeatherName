from apscheduler.schedulers.blocking import BlockingScheduler
from twitter_name import update_twitter_name
import time

# Twitter
consumer_key=''
consumer_secret=''
access_token=''
access_token_secret=''
# replace "-weather-" to emoji, so insert "-weather-" to your name
name="xx-weather-xx"
# OpenWeatherMap
cityid=''
appid=''

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
# Sample
# update twitter name every 10 seconds
scheduler.add_job(job, 'interval', seconds=10)
# at 12:00
#scheduler.add_job(job, 'cron', day_of_week='1-7', hour=12, minute=00)

scheduler.start()