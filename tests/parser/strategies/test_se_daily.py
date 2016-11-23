import unittest
from parser import Parser
from parser.strategies import SEDaily

class TestSEDaily(unittest.TestCase):
    def setUp(self):
        with open("tests/support/se_daily_newsletter.html") as f:
            self.parser = Parser(f.read(), SEDaily)

    def test_correct_number_of_articles_is_parsed(self):
        self.assertEqual(len(self.parser.articles()), 24)


if __name__ == "__main__":
    unittest.main(verbosity=2)
