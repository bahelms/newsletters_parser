class Message(object):
    """Container for Gmail API message response data."""

    def __init__(self, data):
        self.data = data

    def body(self):
        return self.data["raw"].encode("ASCII")
