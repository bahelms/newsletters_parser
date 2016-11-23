import httplib2
from . import Auth, Message
from apiclient import discovery

ARCHIVED = "Label_1"


class Client(object):
    """Interface to Gmail API"""

    def __init__(self, user_id):
        self.service = self._setup_service()
        self.messages = self.service.users().messages()
        self.user_id = user_id

    def retrieve_messages(self):
        """Retrieve data for all active messages in inbox"""
        query = "label:inbox"
        for id in self.message_ids(query):
            yield self.get_message(id)

    def message_ids(self, query=""):
        """Returns a list of ids for messages in inbox scoped to query"""
        data = self.messages.list(userId=self.user_id, q=query).execute()
        return [ids["id"] for ids in data["messages"]]

    def get_message(self, msg_id):
        """Retrieves a specified gmail message"""
        args = {"userId": self.user_id, "id": msg_id, "format": "full"}
        msg = self.messages.get(**args).execute()
        return Message(msg)

    def archive(self, msg_id):
        """Removes Inbox label and adds Archived label"""
        body = {"removeLabelIds": ["INBOX"], "addLabelIds": [ARCHIVED]}
        self.messages.\
            modify(userId=self.user_id, id=msg_id, body=body).execute()

    def _setup_service(self):
        http = Auth().credentials().authorize(httplib2.Http())
        return discovery.build("gmail", "v1", http=http)
