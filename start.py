from apscheduler.schedulers.blocking import BlockingScheduler
from twitter_name import update_twitter_name

# Twitter
consumer_key=''
consumer_secret=''
access_token=''
access_token_secret=''
twitter_name=''
# OpenWeatherMap
cityid=''
appid=''

def job():
    """
    Scheduler job
    :return:
    """
    update_twitter_name(consumer_key,consumer_secret,
                        access_token,access_token_secret,
                        cityid,appid,
                        twitter_name)

scheduler = BlockingScheduler()
# Sample
# update twitter name at 8:00, 12:00
scheduler.add_job(job, 'cron', day_of_week='1-7', hour=8, minute=00)
scheduler.add_job(job, 'cron', day_of_week='1-7', hour=12, minute=00)

scheduler.start()