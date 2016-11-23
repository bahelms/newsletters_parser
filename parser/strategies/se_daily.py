from parser.strategies.parsing_strategy import ParsingStrategy


class SEDaily(ParsingStrategy):
    """HTML parsing strategy for Software Engineering Daily Newsletter"""

    def parsed_articles(self):
        """Returns a list of dicts containing article data

        :returns: List[bs4.element.Tag]
        """
        raise NotImplementedError("parsed_articles")

    def article_format(_self, article):
        """Returns dictionary of article data

        :article: bs4.element.Tag
        :returns: {"url": str, "title": str, "snippet": str}
        """
        raise NotImplementedError("article_format")
