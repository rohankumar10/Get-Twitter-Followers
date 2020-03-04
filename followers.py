import tweepy
import csv


#Your Twitter API keys go here
consumer_key = 'XXXXXXXX'
consumer_secret = 'XXXXXXXX'
access_token = 'XXXXXXXX'
access_secret ='XXXXXXXX'

twitter_handle = 'MesutOzil1088' # Any Username

auth = tweepy.auth.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

f = csv.writer(open('followers.csv', 'w'))

f.writerow(["screenName", "name", "location", "description"])

users = tweepy.Cursor(api.followers, screen_name=twitter_handle, count = 200).items()

for u in users:
    twtHandle = u.screen_name
    name = u.name
    location = u.location
    try:
      f.writerow([twtHandle, name, location])
    except UnicodeEncodeError:
      pass
      
