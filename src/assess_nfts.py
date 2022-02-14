from utils import handles_to_ids, TWITTER, DISCORD
import time
import datetime

"""
Add the handle of NFT Collections. The script will return how many followers it has for level 1,2 & 3.
"""

nft_collections_handle = ["RagnarokMeta"]
nft_collections_ids = handles_to_ids(nft_collections_handle)

LEVEL_1_ID = "1493246044662112258"
LEVEL_2_ID = "1493242833087696904"
LEVEL_3_ID = "1493246190028263434"

LEVEL_1_USER_IDS = [user.__dict__["id"] for user in TWITTER.get_list_members(list_id=LEVEL_1_ID).__dict__["data"]]
LEVEL_2_USER_IDS = [user.__dict__["id"] for user in TWITTER.get_list_members(list_id=LEVEL_2_ID).__dict__["data"]]
LEVEL_3_USER_IDS = [user.__dict__["id"] for user in TWITTER.get_list_members(list_id=LEVEL_3_ID).__dict__["data"]]

level_1_intersection_ids = []
level_2_intersection_ids = []
level_3_intersection_ids = []
nft_data_container = {}
for id_ in nft_collections_ids:
    nft_data_container[id_] = {"level_1_follower_ids": [], "level_2_follower_ids": [], "level_3_follower_ids": [],
                               "total_follows": 0}
    next_token = "initial"
    total_follows = 0
    followers = []
    while next_token:
        if next_token == "initial":
            follows_full_data = TWITTER.get_followers(user_id=id_, max_results=1000).__dict__
        else:
            follows_full_data = TWITTER.get_followers(user_id=id_, max_results=1000, pagination_token=next_token).__dict__
        next_token = follows_full_data["meta"].__dict__["next_token"]
        followers += follows_full_data["data"]
        total_follows += 1000
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print(f"ID: {id_} is followed by {total_follows} users. Current time is: {current_time}")
        time.sleep(60 * 15)  # necessary limit for querying twitter API
    nft_data_container[id_]["total_follows"] = total_follows
    followers = [followers[i].__dict__["id"] for i in range(len(followers))]
    for follower in followers:
        if follower in LEVEL_1_USER_IDS:
            nft_data_container[id_]["level_1_follower_ids"].append(follower)
        elif follower in LEVEL_2_USER_IDS:
            nft_data_container[id_]["level_2_follower_ids"].append(follower)
        elif follower in LEVEL_3_USER_IDS:
            nft_data_container[id_]["level_3_follower_ids"].append(follower)

    total_level_1_follows = len(nft_data_container[id_]["level_1_follower_ids"])
    total_level_2_follows = len(nft_data_container[id_]["level_2_follower_ids"])
    total_level_3_follows = len(nft_data_container[id_]["level_3_follower_ids"])

    nft_collection_handle = TWITTER.get_user(user_id="1432402638868389892").__dict__["data"].__dict__["username"]

    DISCORD.send(f"Hey DAS, NFT Collection {nft_collection_handle}, is followed by "
                 f"{total_level_1_follows}, {total_level_2_follows}, {total_level_3_follows} "
                 f"L1, L2 and L3 followers respectively.")


