#!/bin/python
import asyncio
import sys
import os
import logging
from dotenv import load_dotenv
import telegram

log_filename=sys.argv[1] # first command line argument

logging.basicConfig(
    filename=log_filename,
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger(__name__)


AMOUNT = 3.6
REMINDER_MSG = f"Bitte bezahlen:\nhttps://www.paypal.com/paypalme/FelixDobler/{AMOUNT}"

async def main():
    bot = telegram.Bot(os.getenv('TELEGRAM_API_TOKEN'))
    async with bot:

        logger.info('Sending message: %s', REMINDER_MSG)
        try:
            # await asyncio.sleep(10)
            await bot.send_message(text=REMINDER_MSG, chat_id=os.getenv('GROUP_ID'))
            logger.info('Sent reminder')
        except Exception as ex:
            logger.error('Sending reminder failed: %s', ex)


if __name__ == '__main__':
    load_dotenv()
    asyncio.run(main())
