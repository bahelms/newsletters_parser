import httplib2
from parser.gmail import Auth
from apiclient import discovery

class Client(object):
    """Interface to Gmail API"""

    def __init__(self, user_id):
        self.service = self._setup_service()
        self.user_id = user_id

    def retrieve_messages(self):
        """Retrieve data for all messages in inbox"""
        return [self.get_message(id) for id in self.message_ids()]

    def message_ids(self):
        """Returns a list of ids for all messages in inbox"""
        messages = self.service.users().messages()
        return messages.list(userId=self.user_id).execute()

    def get_message(self, id):
        """Retrieves a specified gmail message"""
        return id

    def _setup_service(self):
        http = Auth().credentials().authorize(httplib2.Http())
        return discovery.build("gmail", "v1", http=http)
