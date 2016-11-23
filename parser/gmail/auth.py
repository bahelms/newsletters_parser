import os
import logging
from oauth2client import client, tools
from oauth2client.file import Storage

SCOPES = ["https://www.googleapis.com/auth/gmail.modify"]
CLIENT_SECRET = "client_secret.json"
APP = "Newsletter Retrieval"
logger = logging.getLogger(__name__)


class Auth(object):
    """Setup the proper credentials for Gmail API authorization"""

    def authorize_connection(self, http):
        return self.credentials().authorize(http)

    def credentials(self):
        """Gets valid user credentials from storage.

        If nothing has been stored, or if the stored credentials are invalid,
        the OAuth2 flow is completed to obtain the new credentials.

        Returns:
            Credentials, the obtained credential.
        """
        credentials_path = os.path.join(os.getcwd(), "transfer_creds.json")
        store = Storage(credentials_path)
        credentials = store.get()

        if not credentials or credentials.invalid:
            flow = client.flow_from_clientsecrets(CLIENT_SECRET, SCOPES)
            flow.user_agent = APP
            args = tools.argparser.parse_args()
            args.noauth_local_webserver = True
            credentials = tools.run_flow(flow, store, args)
            logger.info("Storing credentials to {0}".format(credentials_path))
        return credentials
