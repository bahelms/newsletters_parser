import unittest
from parser.strategies import gmail

class TestGmailMessage(unittest.TestCase):
    def setUp(self):
        self.message = gmail.Message(self.data())

    def test_body(self):
        self.assertEqual(self.message.body(), "Hey there, bo")

    def data(self):
        return {
            "payload": {
                "parts": [{
                    "body": {"data": "Hey there, bo"}
                }, {
                    "body": {"data": "Guess who's coming to dinner?"}
                }]
            }
        }

if __name__ == "__main__":
    unittest.main()
