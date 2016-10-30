import logging
from lxml import etree
from typing import Tuple

logger = logging.getLogger(__name__)

class Parser(object):
    """Extracts data for articles from HTML strings"""

    def __init__(self, html: str):
        """Takes a string of HTML"""
        self.html = html

    def articles(self):
        """Returns a list of dictionaries containing article data

        :returns: List[Dict]
        """
        return [{}]
