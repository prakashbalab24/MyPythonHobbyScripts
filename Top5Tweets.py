import twitter
import os
from twisted.internet import task, reactor

APP_TITLE = "Top 5 India Trending"

CONSUMER_KEY = '<---------->'
CONSUMER_SECRET_KEY = '<---------->'
ACCESS_TOKEN = '<---------->'
ACCESS_TOKEN_SECRET = '<---------->'
INDIA_WOEID = '<---------->'
TIME_OUT = 1800.0

def notify(title, text):
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))


def getTopTweetandDisplay():
    api = twitter.Api(consumer_key=CONSUMER_KEY,
                      consumer_secret=CONSUMER_SECRET_KEY,
                      access_token_key=ACCESS_TOKEN,
                      access_token_secret=ACCESS_TOKEN_SECRET)

    # print(api.VerifyCredentials())

    trends = api.GetTrendsWoeid(woeid=INDIA_WOEID)
    ten_trends = ""

    for i in range(0, 5):
        print(trends[i].name)
        ten_trends = trends[i].name
        notify(APP_TITLE, str(i + 1) + "  " + ten_trends)
    pass

l = task.LoopingCall(getTopTweetandDisplay)
l.start(TIME_OUT)
reactor.run()

# api = twitter.Api(consumer_key=CONSUMER_KEY,
#                       consumer_secret=CONSUMER_SECRET_KEY,
#                       access_token_key=ACCESS_TOKEN,
#                       access_token_secret=ACCESS_TOKEN_SECRET)
# api.PostUpdate("Tweet from Python script! #python #pythonscript #pythonlove #programming #learning")
#
