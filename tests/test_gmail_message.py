import unittest
from parser.gmail_message import GmailMessage

class TestGmailMessage(unittest.TestCase):
    def test_body(self):
        self.assertEqual(self.message.body, "hey there, bo")
