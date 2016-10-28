class Parser(object):
    """Parses HTML strings into Article models"""

    def __init__(self, message):
        """
        :message: HTML string
        :returns: Article model

        """
        self.message = message
