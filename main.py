import logging
import os
import sys
from parser import gmail, Parser
from parser.database import Database
from parser.pending_article import PendingArticle
from parser.strategies import *

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info("Parser started.")

user_id = os.environ["GMAIL_USER_ID"]
client = gmail.Client(user_id)
db = Database(os.environ["PARSER_ENV"])

db.initialize()

for message in client.retrieve_messages():
    strategy_name = message.newsletter_name().replace(" ", "")

    if strategy_name in dir():
        strategy = getattr(sys.modules[__name__], strategy_name)
        for article in Parser(message.html(), strategy).articles():
            db.persist(PendingArticle(**article))
        client.archive(message.id)
    else:
        logger.info("No strategy found for {}".format(strategy_name))
