import logging
import os
import sys
from parser import gmail, Parser
from parser.strategies import PycodersWeekly
from parser.pending_article import PendingArticle

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info("Parser started.")

user_id = os.environ["GMAIL_USER_ID"]
client = gmail.Client(user_id)
msg_ids = client.message_ids()

for id in msg_ids:
    message = client.get_message(id)
    strategy_name = message.newsletter_name().replace(" ", "")

    if strategy_name in dir():
        strategy = getattr(sys.modules[__name__], strategy_name)
        for article in Parser(message.html(), strategy).articles():
            pending_article = PendingArticle(**article)
            logger.info(pending_article.title)
            # save articles
        # archive email
    else:
        logger.info("No strategy found for {}.".format(strategy_name))
