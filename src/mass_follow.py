from utils import handles_to_ids, TWITTER, DISCORD, TWITTER_URL
import time
import datetime
import requests
from requests_oauthlib import OAuth1
import os

"""
Add the twitter handles of your area experts. The script will return a list of handles to follow.
"""
PAGE_TOKEN = 2

auth = OAuth1(
        client_key=os.getenv('dimireadsthings_oauth_consumer_key'),
        client_secret=os.getenv('dimireadsthings_oauth_consumer_key_secret'),
        resource_owner_key=os.getenv('dimireadsthings_oauth_token'),
        resource_owner_secret=os.getenv('dimireadsthings_oauth_token_secret')
)

handle_of_base_accounts = ["gmoneyNFT"]
id_of_trusted_accounts = handles_to_ids(handles=handle_of_base_accounts)
follows_full_data = TWITTER.get_following(user_id=id_of_trusted_accounts[0], max_results=1000, pagination_token=PAGE_TOKEN).__dict__
follows_users = follows_full_data["data"]
follows = [follows_users[i].__dict__["id"] for i in range(len(follows_users))]
for friend in follows:

    params = {
        'user_id': str(friend),
        'follow': 'true',
    }

    response = requests.post('https://api.twitter.com/1.1/friendships/create.json', params=params, auth=auth)
