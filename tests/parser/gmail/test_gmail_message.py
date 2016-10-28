import unittest
import base64
from parser import gmail

class TestGmailMessage(unittest.TestCase):
    def setUp(self):
        self.message = gmail.Message(self.data())

    def test_html(self):
        self.assertEqual(self.message.html(), "<div>Hey there</div>")

    def data(self):
        return {
            "payload": {
                "parts": [{
                    "mimeType": "text/html",
                    "body": {"data": base64.b64encode(b"<div>Hey there</div>")},
                }, {
                    "mimeType": "text/plain",
                    "body": {"data": "not html"}
                }]
            }
        }

if __name__ == "__main__":
    unittest.main()
