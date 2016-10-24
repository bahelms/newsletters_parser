from parser.strategies import gmail

class Strategy(object):
    """Methods for interacting with the Gmail API"""

    def __ini__(self):
        pass

    def message(self, response):
        return gmail.Message(response)
