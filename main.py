import logging
from parser.gmail_client import GmailClient

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info("Parser started.")

client = GmailClient()
for message in client.messages():
    logger.info(message.body())
    # decode
    # parse articles
    # save articles
    # archive email
