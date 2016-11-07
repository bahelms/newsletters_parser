import base64
import re

class Message(object):
    """Container for Gmail API message response data."""

    def __init__(self, data):
        self.data = data
        self.headers = data["payload"]["headers"]
        self.source_pattern = re.compile("(.+)\s(<.+>)")

    def html(self):
        """Returns message in HTML format

        :returns: UTF-8 HTML string
        """
        html_bytes = base64.urlsafe_b64decode(self._encoded_html_data())
        return html_bytes.decode("utf-8")

    def newsletter_name(self):
        """Returns the name of the newsletter taken from 'From' header

        :returns: String
        """
        return self.source_pattern.match(self._message_source()).group(1)

    def newsletter_source(self):
        """Returns the source email address

        :returns: String
        """
        return self.source_pattern.match(self._message_source()).group(2)

    def _encoded_html_data(self):
        """Extracts encoded HTML bytes data from message

        :returns: Base64 encoded bytes
        """
        html_type = lambda part: part["mimeType"] == "text/html"
        html_part = list(filter(html_type, self.data["payload"]["parts"]))[0]
        return html_part["body"]["data"]

    def _message_source(self):
        """Returns the full value for the message source destination

        :returns: String
        """
        return next(
            header["value"]
            for header in self.headers
            if header["name"] == "From")
