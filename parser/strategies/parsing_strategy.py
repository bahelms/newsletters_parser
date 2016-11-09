class ParsingStrategy(object):
    """Abstract class for HTML parsing methods"""

    def __init__(self, html):
        """Implementation strategy for parsing specific HTML layouts

        :html: Parsing object containing a representation of HTML
        """
        self.html = html

    def parsed_articles(self):
        """Returns a list of dicts containing article data

        :returns: List[bs4.element.Tag]
        """
        raise NotImplementedError("parsed_articles")

    def article_format(_self, article):
        """Returns dictionary of article data

        :article: bs4.element.Tag
        :returns: Dict
        """
        raise NotImplementedError("article_format")
