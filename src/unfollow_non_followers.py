from utils import handles_to_ids, TWITTER,\
    DISCORD, TWITTER_URL, TWITTER_OAUTH_CONSUMER_KEY, TWITTER_OAUTH_CONSUMER_KEY_SECRET,\
    TWITTER_OAUTH_TOKEN, TWITTER_OAUTH_TOKEN_SECRET
import time
import datetime
import requests
from requests_oauthlib import OAuth1
import os

"""
Add the twitter handles of your area experts. The script will return a list of handles to follow.
"""

auth = OAuth1(
        client_key=TWITTER_OAUTH_CONSUMER_KEY,
        client_secret=TWITTER_OAUTH_CONSUMER_KEY_SECRET,
        resource_owner_key=TWITTER_OAUTH_TOKEN,
        resource_owner_secret=TWITTER_OAUTH_TOKEN_SECRET
)

handle_of_base_accounts = ["hip_munks"]
id_of_trusted_accounts = handles_to_ids(handles=handle_of_base_accounts)
next_token = "initial"
followers = []
thousand_followers_counter = 0
while thousand_followers_counter < 1:
    if next_token == "initial":
        follows_full_data = TWITTER.get_followers(user_id=id_of_trusted_accounts[0], max_results=1000).__dict__
    else:
        follows_full_data = TWITTER.get_followers(user_id=id_of_trusted_accounts[0], max_results=1000, pagination_token=next_token).__dict__
    follows_users = follows_full_data["data"]
    next_token = follows_full_data["meta"].__dict__["next_token"]
    follows = [follows_users[i].__dict__["id"] for i in range(len(follows_users))]
    followers += follows
    thousand_followers_counter += 1

next_token = "initial"
thousand_followers_counter = 0
friends = []
while thousand_followers_counter < 1:
    if next_token == "initial":
        follows_full_data = TWITTER.get_following(user_id=id_of_trusted_accounts[0], max_results=1000).__dict__
    else:
        follows_full_data = TWITTER.get_following(user_id=id_of_trusted_accounts[0], max_results=1000, pagination_token=next_token).__dict__
    follows_users = follows_full_data["data"]
    next_token = follows_full_data["meta"].__dict__["next_token"]
    follows = [follows_users[i].__dict__["id"] for i in range(len(follows_users))]
    friends += follows
    thousand_followers_counter += 1

for f in friends:
    if f not in followers:

        params = {
            'user_id': f,
            'follow': 'true',
        }

        response = requests.post('https://api.twitter.com/1.1/friendships/destroy.json', params=params, auth=auth)
        print(response.json())
        print(f)

