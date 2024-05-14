import os

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('BOT_TOKEN')
ADMIN_LIS = os.getenv('ADMIN_ID')
CHANNEL = os.getenv('CHANNEL_ID')

