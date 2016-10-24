from parser.gmail_message import GmailMessage

class TestStrategy(object):
    """An email client strategy to mock real email services"""

    def message(self, response):
        return GmailMessage(response)

    def message_stub(self):
        return {
            "id": "157e83af33bf13ea",
            "threadId": "157e83af33bf13ea",
            "labelIds": ["INBOX", "UNREAD"],
            "snippet": "Subject: This week&#39;s Ruby news, issue 318 Date: Thu, 6 Oct 2016 18:46:10 +0000 From: Ruby Weekly &lt;rw@peterc.org&gt; Reply-To: Ruby Weekly &lt;rw@peterc.org",
            "payload": {
                "mimeType": "multipart/alternative",
                "filename": "",
                "headers": [],
                "body": {},
                "parts": [
                    {
                        "partId": "0",
                        "mimeType": "text/plain",
                        "filename": "",
                        "headers": [{"name": "", "value": ""}],
                        "body": {"size": "123", "data": "DQoNCg0KLS0tLS0tLS0"}
                    }, {
                        "partId": "1",
                        "mimeType": "text/html",
                        "filename": "",
                        "headers": [{"name": "", "value": ""}],
                        "body": {"size": "123", "data": "kgDQo8aHR0cDovL3J1Y"}
                    }
                ]
            }
        }
