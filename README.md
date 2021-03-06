# Affirmation Telegram Bot

This program sends an affirmation message to a Telegram channel using a Telegram Bot.

__UPDATE:__ No longer uses https://affirmations.dev but instead uses a list of affirmations gleaned from various websites. The APi at affirmations.dev was far too repetitive.

Implementation at https://t.me/AffirmationToday

## Setup

1. See https://core.telegram.org/bots#3-how-do-i-create-a-bot for how to create a telegram bot.

1. Zip the following into a file called lambda_files.zip and upload it as a Lambda function. See https://aws.amazon.com/premiumsupport/knowledge-center/build-python-lambda-deployment-package/ under '__Upload deployment package to your Lambda function__':
   1. all requirements from requirements_lambda.txt 
   1. affirmation_bot_lambda.py and
   1. affirmation_list.txt 
1. Set the AWS Lambda handler/entry point to "affirmation_bot_lambda.lambda_handler".

1. Add the API_KEY and CHANNEL_NAME environment variables in the editor. CHANNEL_NAME can be obtained by adding a "@" to the beginning of the segment of the public Telegram channel URL after "t.me". Note that the bot must be set to an admin in the Telegram channel. See also https://stackoverflow.com/questions/33858927/how-to-obtain-the-chat-id-of-a-private-telegram-channel

1. Set a rule to trigger according to a CloudWatch Event where you can set a time of day to send the relevant message.