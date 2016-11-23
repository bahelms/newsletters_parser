from parser.strategies.parsing_strategy import ParsingStrategy


class PycodersWeekly(ParsingStrategy):
    """HTML parsing strategy for Pycoders Weekly Newsletter"""

    def parsed_articles(self):
        """Returns a list of dicts containing article data

        :returns: List[bs4.element.Tag]
        """
        tables = self.html.find_all("table", class_="mcnTextContentContainer")
        res = [
            [a for a in table.find_all("a") if a.has_attr("target")]
            for table in tables
            if table.h2 and table.h2.text != "Python Jobs"]

        return [self.article_format(a) for sublist in res for a in sublist]

    def article_format(_self, article):
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
