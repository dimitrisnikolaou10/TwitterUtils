from utils import handles_to_ids, TWITTER, DISCORD, DASFORNFT_ID, TWITTER_URL
import time
import datetime

"""
Create a set of the last 5 follows of each of Level 1 user, remove users you already follow and return the rest .
This is based on the fact that Twitter API returns list of following, sorted in the order you followed.
"""

LEVEL_1_ID = "1493246044662112258"

LEVEL_1_USER_IDS = [user.__dict__["id"] for user in TWITTER.get_list_members(list_id=LEVEL_1_ID).__dict__["data"]]

ALREADY_FOLLOWING = [user.__dict__["id"] for user in TWITTER.get_following(user_id=DASFORNFT_ID, max_results=250).__dict__["data"]]

new_follow_list = []
for user_id in LEVEL_1_USER_IDS:
    print(f"Currently assessing user id {user_id}.")
    new_following = [user.__dict__["id"] for user in TWITTER.get_following(user_id=user_id, max_results=5).__dict__["data"]]
    new_follow_list += new_following
    time.sleep(60*15)  # necessary limit for querying twitter API

set_of_new_follows = list(set(new_follow_list) - set(ALREADY_FOLLOWING))

new_follows = [TWITTER.get_user(user_id=u_id).__dict__["data"].__dict__["username"] for u_id in set_of_new_follows]

new_follows_twitter_url = [TWITTER_URL + handle for handle in new_follows]

DISCORD.send("New users to follow:")
for handle in new_follows_twitter_url:
    DISCORD.send(handle)
