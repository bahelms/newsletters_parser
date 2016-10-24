class EmailClient(object):
    """Interface to Email API"""

    def __init__(self, strategy):
        self.strategy = strategy

    def message_ids(self):
        """Returns a list of ids for all messages in inbox"""
        return []

    def messages(self):
        """List full data for all messages in inbox"""
        return [self.get_message(id) for id in self.message_ids()]

    def get_message(self, id):
        """Request email message and return strategy message object"""
        response = {}
        return self.strategy.message(response)

    # def _setup_service(self, auth):
    #     http = auth.authorize_connection(httplib2.Http())
    #     return discovery.build("gmail", "v1", http=http)
