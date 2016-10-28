import httplib2
import logging
from . import Auth, Message
from apiclient import discovery

class Client(object):
    """Interface to Gmail API"""

    def __init__(self, user_id):
        self.service = self._setup_service()
        self.messages = self.service.users().messages()
        self.user_id = user_id

    def retrieve_messages(self):
        """Retrieve data for all messages in inbox"""
        return [self.get_message(id) for id in self.message_ids()]

    def message_ids(self):
        """Returns a list of ids for all messages in inbox"""
        data = self.messages.list(userId=self.user_id).execute()
        return [ids["id"] for ids in data["messages"]]

    def get_message(self, msg_id):
        """Retrieves a specified gmail message"""
        args = {"userId": self.user_id, "id": msg_id, "format": "full"}
        msg = self.messages.get(**args).execute()
        return Message(msg)

    def _setup_service(self):
        http = Auth().credentials().authorize(httplib2.Http())
        return discovery.build("gmail", "v1", http=http)
