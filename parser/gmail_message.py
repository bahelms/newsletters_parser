class GmailMessage(object):
    """Container for Gmail API message response data."""

    def __init__(self, data):
        self.data = data
        self.content = data["payload"]["parts"]

    def body(self):
        return self.content[0]["body"]["data"]
