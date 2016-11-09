import logging
import re
from bs4 import BeautifulSoup
from parser.strategies import ParsingStrategy

logger = logging.getLogger(__name__)

class Parser(object):
    """Extracts data for articles from HTML strings"""

    def __init__(self, html: str, strategy: ParsingStrategy):
        """Takes a string of HTML and a parsing strategy

        :html: HTML string
        :strategy: Strategy object implementing HTML specific parsing steps
        """
        self.html = BeautifulSoup(html, "lxml")
        self.strategy = strategy(self.html)

    def articles(self):
        """Returns a list of dicts containing article data

        :returns: List[bs4.element.Tag]
        """
        return self.strategy.parsed_articles()
