from utils import handles_to_ids, TWITTER, DISCORD
import time
import datetime

"""
Add the twitter handles of your area experts. The script will return a list of handles to follow.
"""

handle_of_trusted_accounts = ["gmoneyNFT", "DeezeFi", "CozomoMedici", "Vince_Van_Dough"]
id_of_trusted_accounts = handles_to_ids(handles=handle_of_trusted_accounts)

follows_of_trusted_accounts = {}
list_of_follows_of_trusted_accounts = []
for id_ in id_of_trusted_accounts:
    next_token = "initial"
    follows_users = []
    follows_count = 0
    while next_token:
        if next_token == "initial":
            follows_full_data = TWITTER.get_following(user_id=id_, max_results=1000).__dict__
        else:
            follows_full_data = TWITTER.get_following(user_id=id_, max_results=1000, pagination_token=next_token).__dict__
        follows_count += 1000
        next_token = follows_full_data["meta"].__dict__["next_token"]
        follows_users += follows_full_data["data"]
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print(f"ID: {id_} follows {follows_count} users. Current time is: {current_time}")
        time.sleep(60*15)  # necessary limit for querying twitter API
    follows = [follows_users[i].__dict__["id"] for i in range(len(follows_users))]
    follows_of_trusted_accounts[id_] = follows
    list_of_follows_of_trusted_accounts.append(set(follows))

curated_twitter_follows = list(set.intersection(*list_of_follows_of_trusted_accounts))
curated_twitter_follows_handle = [TWITTER.get_user(user_id=u_id).__dict__["data"].__dict__["username"] for u_id in curated_twitter_follows]

DISCORD.send(f"Hey DAS, based on handles: {handle_of_trusted_accounts}, you should follow {curated_twitter_follows_handle}.")
