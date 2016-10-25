import logging
import os
from parser import gmail

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info("Parser started.")

user_id = os.environ["GMAIL_USER_ID"]

client = gmail.Client(user_id)
logger.info(client.message_ids())
# for message in client.retrieve_messages():
#     logger.info(message.body())
    # decode
    # parse articles
    # save articles
    # archive email
