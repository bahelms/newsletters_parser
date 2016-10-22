import unittest
from parser.gmail_client import GmailClient

class TestGmailClient(unittest.TestCase):
    def setUp(self):
        self.client = GmailClient()

    def test_retrieving_list_of_all_message_ids(self):
        self.assertEqual(self.client.message_ids(), self.expected_message_ids())

    def test_retrieving_all_messages(self):
        messages = self.client.messages()
        self.assertEqual(len(messages), 2)

    def test_retrieving_content_for_all_messages(self):
        msg_content = [msg.body for msg in self.client.messages()]
        self.assertEqual(msg_content[0], "DQoNCg0KLS0tLS0tLS0")
        self.assertEqual(msg_content[1], "kgDQo8aHR0cDovL3J1Y")

    def expected_message_ids(_):
        return {
            "messages": [
                {"id": "157e3d65eed7eac1"},
                {"id": "157e3532a4f149b0"},
            ]
        }

if __name__ == "__main__":
    unittest.main()
