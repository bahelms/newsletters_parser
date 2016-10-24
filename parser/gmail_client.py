import httplib2
from apiclient import discovery
from parser.gmail_message import GmailMessage
from parser.gmail_auth import GmailAuth

class GmailClient(object):
    """Interface to Gmail API"""

    def __init__(self):
        self.service = self.setup_service(GmailAuth())

    def setup_service(self, auth):
        http = auth.authorize_connection(httplib2.Http())
        return discovery.build("gmail", "v1", http=http)

    def message_ids(self):
        """Returns a list of ids for all messages in inbox"""
        # self.service
        return self.message_ids_stub()

    def messages(self):
        """List full data for all messages in inbox"""
        return [self.retrieve_message(id) for id in self.message_ids()]

    def retrieve_message(self, id):
        """Request Gmail API message and return GmailMessage object"""
        # make request
        return GmailMessage(self.message_stub())


    """Temporary data stubs"""

    def message_ids_stub(self):
        return ["157e3d65eed7eac1", "157e3532a4f149b0"]

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
