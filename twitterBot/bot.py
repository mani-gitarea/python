import tweepy as tp
import time
import os

cons_api_key='XG2TFe6aoVryVkCAfinGmsNlZ'
cons_api_secret_key='5ECezp3wmUnPUVF3JdPDVJHADhf1KswdD3Wk6VfwN8Ti9uqW9x'
access_token='1070625346586927104-jTh4G31oHHQXqasM3Yr1HFsI9xK9uC'
access_token_secret='UlbEO5HpCwd3U9KdvFvivAQNn4fC8LG3EMU7ilFG2L2CU'

auth = tp.OAuthHandler(cons_api_key,cons_api_secret_key)
auth.set_access_token(access_token,access_token_secret)
api = tp.API(auth)
x = 0

#Read existing tweets and delete all the tweets
tweets = api.user_timeline()
if len(tweets) > 0:
    for i in tweets:
        api.destroy_status(tweets[x]._json["id"])
        x += 1

#Post Tweets

os.chdir('pictures/pexels')
for image in os.listdir('.'):
    api.update_with_media(image)
    time.sleep(10)