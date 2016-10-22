class GmailClient(object):
    """Interface to Gmail API"""

    def message_ids(self):
        """Returns a list of ids for all messages in inbox"""
        return self.message_ids_stub()

    def messages(self):
        """List full data for all messages in inbox"""
        pass

    def message_ids_stub(self):
        return {
            "messages": [
                {"id": "157e3d65eed7eac1"},
                {"id": "157e3532a4f149b0"},
            ]
        }

    def messages_stub(self):
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
                        "body": {"size": "123", "data": "DQoNCg0KLS0tLS0tLS0"}
                    }
                ]
            }
        }
