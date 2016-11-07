import logging
import re
from bs4 import BeautifulSoup
from parser import ParsingStrategy

logger = logging.getLogger(__name__)

class Parser(object):
    """Extracts data for articles from HTML strings"""

    def __init__(self, html: str, strategy: ParsingStrategy):
        """Takes a string of HTML

        :html: HTML string
        :strategy: Strategy object implementing HTML specific parsing steps
        """
        self.html = BeautifulSoup(html, "lxml")

    def articles(self):
        """Returns a list of dicts containing article data

        :returns: List[bs4.element.Tag]
        """
        tables = self.html.find_all("table", class_="mcnTextContentContainer")
        res = [
            [a for a in table.find_all("a") if a.has_attr("target")]
            for table in tables
            if table.h2 and table.h2.text != "Python Jobs"]

        return [self.article_format(a) for sublist in res for a in sublist]

    @staticmethod
    def article_format(article):
        """Returns dictionary of article data

        :article: bs4.element.Tag
        :returns: Dict
        """
        snippet = article.next_sibling.next_sibling.next_sibling.next_element
        return {
            "url": article["href"],
            "title": article.next_element.next_element,
            "snippet": snippet
            }
