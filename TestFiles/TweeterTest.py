import tweepy
import json
from twitter import *
from tweepy import OAuthHandler


consumer_key = 'Pqa4IkRATQIQI5cmeoku9uSmc'
consumer_secret = 'sQ0RfURq56xQIxU4Zo3EbsMtYuN127YeujlR5aXnznwatkUkYr'
access_token = '878801066749378560-xxVM1tzuOBSSwlPVYrtEGcpHuPFSWzO'
access_secret = '51qMwcwcOoBZwQqtWIpIKFOROGgjphpdZTAR80DhvbRwD'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)


#for status in tweepy.Cursor(api.home_timeline).items(10):
    # Process a single status
   # print(status.text)
  # pass

trendss = api.trends_place(	23424934)
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

dict_trend_list = dict(list(enumerate(trend_list)))
json_trends = json.dumps(dict_trend_list)
print(json_trends)