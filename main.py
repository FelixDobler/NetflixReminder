#!/bin/python
import asyncio
import sys
import os
import logging
from dotenv import load_dotenv
import telegram

log_filename = sys.argv[1]  # first command line argument

logging.basicConfig(
    filename=log_filename,
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger(__name__)

REMINDER_MSG = os.getenv('MESSAGE_TEXT')


async def main():
    """
    Sends a message to a telegram channel the bot is a member of
    """
    bot = telegram.Bot(os.getenv('TELEGRAM_API_TOKEN'))
    async with bot:
        logger.info('Sending message: %s', REMINDER_MSG)
        try:
            await bot.send_message(text=REMINDER_MSG, chat_id=os.getenv('GROUP_ID'))
            logger.info('Sent reminder')
        except Exception as ex:
            logger.error('Sending reminder failed: %s', ex)

if __name__ == '__main__':
    load_dotenv()
    asyncio.run(main())
