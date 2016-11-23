import unittest
import base64
from parser import gmail

class TestGmailMessage(unittest.TestCase):
    def setUp(self):
        self.message = gmail.Message(self.data())

    def test_html(self):
        self.assertEqual(self.message.html(), "<div>Hey there</div>")

    def test_newsletter_name(self):
        self.assertEqual(self.message.newsletter_name(), "Scala Times")

    def test_newsletter_source(self):
        expected_source = "<scalatimes@softwaremill.com>"
        self.assertEqual(self.message.newsletter_source(), expected_source)

    def data(self):
        return {
            "id": "123456",
            "payload": {
                "headers": [{
                    "name": "From",
                    "value": "Scala Times <scalatimes@softwaremill.com>"
                }],
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
    unittest.main(verbosity=2)
