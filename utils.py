"""
UTILITY FUNCTIONS TO BE USED ACROSS PROJECT
"""
import discord
import os
from pytwitter import Api
import dotenv

dotenv.load_dotenv()

DISCORD_WEBHOOK_URL = os.getenv('DISCORD_WEBHOOK_URL')
DISCORD = discord.Webhook.from_url(DISCORD_WEBHOOK_URL, adapter=discord.RequestsWebhookAdapter())
TWITTER_TOKEN = os.getenv('TWITTER_TOKEN')
TWITTER = Api(bearer_token=TWITTER_TOKEN)
TWITTER_URL = "https://twitter.com/"


def handles_to_ids(handles: list):
    id_of_trusted_accounts = [TWITTER.get_users(usernames=handles).__dict__["data"][i].__dict__["id"] for i in range(len(handles))]
    return id_of_trusted_accounts

DASFORNFT_ID = handles_to_ids(["dasdotnft",])[0]
