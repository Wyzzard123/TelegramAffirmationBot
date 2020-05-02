"""
Bot to send affirmations to a Telegram channel as an AWS Lambda function
"""

import os
import requests

API_KEY = os.environ['API_KEY']
CHANNEL_NAME = os.environ['CHANNEL_NAME']


def lambda_handler(event, context):
    affirmation_response = requests.get("https://www.affirmations.dev/")
    message = affirmation_response.json()["affirmation"]
    response = requests.get(f"https://api.telegram.org/bot{API_KEY}/sendMessage?chat_id={CHANNEL_NAME}&text={message}")
    print(response.text)
    return message