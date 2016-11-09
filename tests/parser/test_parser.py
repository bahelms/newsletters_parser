import unittest
from parser import Parser
from parser.strategies import PycodersWeekly

class TestParser(unittest.TestCase):
    def setUp(self):
        with open("tests/support/pycoder_weekly_newsletter.html") as f:
            self.parser = Parser(f.read(), PycodersWeekly)

    def test_correct_number_of_articles_is_parsed(self):
        self.assertEqual(len(self.parser.articles()), 24)

    def test_article_url_is_parsed(self):
        expected_url = (
            "http://pycoders.us4.list-manage2.com/track/click?"
            "u=9735795484d2e4c204da82a29&id=70ef754228&e=2ec7311e6d")
        self.assertEqual(self.parser.articles()[0]["url"], expected_url)

    def test_article_snippet_is_parsed(self):
        expected_snippet = (
            "Get your latest Flask application running in production with "
            "NGinx, Gunicorn and PM2.")
        parsed_snippet = self.parser.articles()[-2]["snippet"]
        self.assertEqual(parsed_snippet, expected_snippet)

    def test_article_title_is_parsed(self):
        expected_title = "PyData DC 2016 Videos"
        self.assertEqual(self.parser.articles()[1]["title"], expected_title)

if __name__ == "__main__":
    unittest.main(verbosity=2)
