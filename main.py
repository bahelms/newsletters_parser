import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info("Parser started.")

# get list of emails
# for email in emails
#     fetch email
#     decode
#     parse articles
#     save articles
#     archive email
