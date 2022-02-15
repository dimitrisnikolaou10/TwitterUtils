"""
UTILITY FUNCTIONS TO BE USED ACROSS PROJECT
"""
import discord
import os
from pytwitter import Api
import dotenv

dotenv.load_dotenv()

WEBHOOK_URL = os.getenv('WEBHOOK_URL')
DISCORD = discord.Webhook.from_url(WEBHOOK_URL, adapter=discord.RequestsWebhookAdapter())
TWITTER_TOKEN = os.getenv('TWITTER_TOKEN')
TWITTER = Api(bearer_token=TWITTER_TOKEN)


def handles_to_ids(handles: list):
    id_of_trusted_accounts = [TWITTER.get_users(usernames=handles).__dict__["data"][i].__dict__["id"] for i in range(len(handles))]
    return id_of_trusted_accounts

