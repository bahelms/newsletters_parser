import logging
import os
from parser import gmail

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info("Parser started.")

user_id = os.environ["GMAIL_USER_ID"]

client = gmail.Client(user_id)
message = client.get_message(client.message_ids()[0])
logger.info(message.html())

# for message in client.retrieve_messages():
#     content = base64.b64decode(message.body())
#     logger.info(content)
    # decode
    # parse articles
    # save articles
    # archive email
