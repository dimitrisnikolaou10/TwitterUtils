"""
UTILITY FUNCTIONS TO BE USED ACROSS PROJECT
"""
import discord
import os
from pytwitter import Api
import dotenv

dotenv.load_dotenv()
TWITTER_USER = 'dimireadsthings'

DISCORD_WEBHOOK_URL = os.getenv('DAS_DISCORD_WEBHOOK_URL')
DISCORD = discord.Webhook.from_url(DISCORD_WEBHOOK_URL, adapter=discord.RequestsWebhookAdapter())
TWITTER_BEARER_TOKEN = os.getenv(f'{TWITTER_USER}_BEARER_TOKEN')
TWITTER_OAUTH_CONSUMER_KEY = os.getenv(f'{TWITTER_USER}_OAUTH_CONSUMER_KEY')
TWITTER_OAUTH_CONSUMER_KEY_SECRET = os.getenv(f'{TWITTER_USER}_OAUTH_CONSUMER_KEY_SECRET')
TWITTER_OAUTH_TOKEN = os.getenv(f'{TWITTER_USER}_OAUTH_TOKEN')
TWITTER_OAUTH_TOKEN_SECRET = os.getenv(f'{TWITTER_USER}_OAUTH_TOKEN_SECRET')
TWITTER = Api(bearer_token=TWITTER_BEARER_TOKEN)
TWITTER_URL = "https://twitter.com/"


def handles_to_ids(handles: list):
    id_of_trusted_accounts = [TWITTER.get_users(usernames=handles).__dict__["data"][i].__dict__["id"] for i in range(len(handles))]
    return id_of_trusted_accounts

DASFORNFT_ID = handles_to_ids(["dasdotnft",])[0]
