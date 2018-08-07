
import tweepy
from tweepy import OAuthHandler
from slacker import Slacker


slack = Slacker('xoxb-410883848613-412108123414-7pqKJ0y8dgrCv1S9EtBSHa43')


def postTopTen():
    tel = getTopTen()
    format_tel = ("\n".join(tel))
   # print(format_tel)
    return format_tel



#function to get top 10
def getTopTen():
    #Authorization
    consumer_key = 'Pqa4IkRATQIQI5cmeoku9uSmc'
    consumer_secret = 'sQ0RfURq56xQIxU4Zo3EbsMtYuN127YeujlR5aXnznwatkUkYr'
    access_token = '878801066749378560-xxVM1tzuOBSSwlPVYrtEGcpHuPFSWzO'
    access_secret = '51qMwcwcOoBZwQqtWIpIKFOROGgjphpdZTAR80DhvbRwD'

    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)

    api = tweepy.API(auth)

    #get top ten
    trendss = api.trends_place(23424934)
    count = 0
    trend_list = []
    for location in trendss:
        for trend in location["trends"]:
            top_trend_name = trend["name"]
            trend_list.append(top_trend_name)
           # print(top_trend_name)
            count += 1
            if count % 10 == 0:
                break

    #dict_trend_list = dict(list(enumerate(trend_list)))
    return trend_list


def postbot():
    slack.chat.post_message('#assignment1', postTopTen())