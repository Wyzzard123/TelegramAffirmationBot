"""
Bot to send affirmations to a Telegram channel as an AWS Lambda function
"""

import os
import requests
import random

API_KEY = os.environ['API_KEY']
CHANNEL_NAME = os.environ['CHANNEL_NAME']


def lambda_handler(event, context):
    with open("affirmation_list.txt") as f:
        message = random.choice(f.readlines()).strip()
    telegram_msg = requests.get(f"https://api.telegram.org/bot{API_KEY}/sendMessage?chat_id={CHANNEL_NAME}&text={message}")
    print(telegram_msg.text)
    return message