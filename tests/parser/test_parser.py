import unittest
from parser import Parser

class TestParser(unittest.TestCase):
    def setUp(self):
        with open("tests/support/html_message.html") as f:
            self.parser = Parser(f.read())

    def test_article_data_is_parsed_from_html(self):
        self.assertEqual(len(self.parser.articles()), 24)

if __name__ == "__main__":
    unittest.main()
