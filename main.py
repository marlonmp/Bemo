from logging import error
from dotenv import load_dotenv
from src.client import Client
import os

if __name__ == '__main__':

    load_dotenv()

    TOKEN = os.environ.get('TOKEN')

    if TOKEN is None: raise error('[ERROR] Error getting token')
    
    client = Client()

    client.run(TOKEN)