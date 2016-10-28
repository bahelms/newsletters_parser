import base64

class Message(object):
    """Container for Gmail API message response data."""

    def __init__(self, data):
        self.data = data

    def encoded_html_data(self):
        """Extracts encoded HTML bytes data from message

        :returns: Base64 encoded bytes
        """
        html_type = lambda part: part["mimeType"] == "text/html"
        html_part = list(filter(html_type, self.data["payload"]["parts"]))[0]
        return html_part["body"]["data"]

    def html(self):
        """Returns message in HTML format

        :returns: UTF-8 HTML string
        """
        html_bytes = base64.urlsafe_b64decode(self.encoded_html_data())
        return html_bytes.decode("utf-8")
