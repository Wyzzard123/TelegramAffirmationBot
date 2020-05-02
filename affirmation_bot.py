"""
Bot to send affirmations to a Telegram channel
"""

import requests
import os
from pathlib import Path
from environ import Env

env = Env()
BASE_DIR = os.getcwd()
if Path(BASE_DIR, '.env').is_file():
    env.read_env(str(Path(BASE_DIR, '.env')))
API_KEY = env('API_KEY', str, '123456789')
CHANNEL_NAME = env('CHANNEL_NAME', str, 'abcdefg')
affirmation_response = requests.get("https://www.affirmations.dev/")
message = affirmation_response.json()["affirmation"]
response = requests.get(f"https://api.telegram.org/bot{API_KEY}/sendMessage?chat_id={CHANNEL_NAME}&text={message}")
print(response.text)
