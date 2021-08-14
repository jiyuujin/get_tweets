from requests_oauthlib import OAuth1Session
from dotenv import load_dotenv
import json
import datetime
import os

load_dotenv()

# Consumer api key
comsumer_api_key = os.getenv('CONSUMER_API_KEY')
# Consumer api secret key
comsumer_api_secret_key = os.getenv('CONSUMER_API_SECRET_KEY')
# bearer token
bearer_token = os.getenv('BEARER_TOKEN')
# Access token
access_token = os.getenv('ACCESS_TOKEN')
# Access token secret
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')

url = 'https://api.twitter.com/1.1/statuses/user_timeline.json'

params = {
    'count': 100,
    'exclude_replies': True,
    'include_rts': False
}

TweetList = []
TodayTweet = ''

twitter = OAuth1Session(
    comsumer_api_key,
    comsumer_api_secret_key,
    access_token,
    access_token_secret)

now = datetime.datetime.now()
yesterday = now - datetime.timedelta(days=-1)
# print(now.strftime('%Y/%m/%d %H:%M:%S'))
# print(yesterday.strftime('%Y/%m/%d %H:%M:%S'))

for i in range(100):
    req = twitter.get(url=url, params=params)
    if req.status_code == 200:
        timeline = json.loads(req.text)
        break
    else:
        print('Error: %d' % req.status_code)
        break

for tweet in timeline:
    format_dt = datetime.datetime.strptime(
        tweet['created_at'],
        '%a %b %d %H:%M:%S +0000 %Y')
    if (format_dt - yesterday).days == -2 and (now - format_dt).days == 0:
        TweetList.append(tweet['text'])
        TodayTweet += tweet['user']['name'] + '\n'
        TodayTweet += tweet['text'] + '\n'
        TodayTweet += datetime.datetime.strftime(
            format_dt,
            '%Y/%m/%d %H:%M:%S') + '\n'
        TodayTweet += '=====\n'

print(TodayTweet)

markdown_path = 'tweets/' + now.strftime('%Y-%m-%d') + '.md'

with open(markdown_path, mode='w', encoding='utf-8') as f:
    f.write(TodayTweet)
