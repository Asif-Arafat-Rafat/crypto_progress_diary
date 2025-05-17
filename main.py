from dotenv import load_dotenv
from binance.client import Client
from date import file_name
import os

load_dotenv()

api_key = os.getenv("Binance_API_KEY")
api_secret = os.getenv("Binance_API_SECRET")

client = Client(api_key, api_secret)
coins={}
account_info = client.get_account()
for balance in account_info['balances']:
    if float(balance['free']) > 0:
        coins[balance['asset']]=float(balance['free'])+float(balance['locked'])
file_name(coins)