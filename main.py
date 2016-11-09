import logging
import os
from parser import gmail, Parser
from parser.strategies import PycodersWeekly

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info("Parser started.")

user_id = os.environ["GMAIL_USER_ID"]
client = gmail.Client(user_id)
msg_ids = client.message_ids()

for id in msg_ids:
    message = client.get_message(id)
    if message.newsletter_name() == "Pycoders Weekly":
        parser = Parser(message.html(), PycodersWeekly)
        logger.info(parser.articles())

# save articles
# archive email
