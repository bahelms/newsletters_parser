import unittest
from parser.email_client import EmailClient

class TestEmailClient(unittest.TestCase):
    def setUp(self):
        self.client = EmailClient(TestStrategy())

    def test_retrieving_list_of_all_message_ids(self):
        expected_message_ids = ["157e3d65eed7eac1", "157e3532a4f149b0"]
        self.assertEqual(self.client.message_ids(), expected_message_ids)

    def test_retrieving_all_messages(self):
        messages = self.client.messages()
        self.assertEqual(len(messages), 2)

    def test_retrieving_content_for_all_messages(self):
        msg_content = [msg.body() for msg in self.client.messages()]
        self.assertEqual(msg_content[0], "DQoNCg0KLS0tLS0tLS0")

if __name__ == "__main__":
    unittest.main()
