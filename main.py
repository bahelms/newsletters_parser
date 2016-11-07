import logging
import os
from parser import gmail, Parser

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info("Parser started.")

user_id = os.environ["GMAIL_USER_ID"]
client = gmail.Client(user_id)
msg_ids = client.message_ids()[:1]

for id in msg_ids:
    message = client.get_message(id)
    logger.info(message.newsletter_name())
    logger.info(message.newsletter_source())

# parse articles
# save articles
# archive email
