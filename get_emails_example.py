import httplib2
import os
from apiclient import discovery
from oauth2client import client, tools
from oauth2client.file import Storage

SCOPES = "https://www.googleapis.com/auth/gmail.readonly"
CLIENT_SECRET = "client_secret.json"
APP = "Newsletter Transfer"
USER_ID = "user_id@gmail.com"

def get_credentials():
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
        credentials = tools.run_flow(flow, store, None)
        print("Storing credentials to {0}".format(credentials_path))
    return credentials

def main():
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build("gmail", "v1", http=http)

    results = service.users().messages().list(userId=USER_ID).execute()
    for data in results["messages"]:
        msgs_service = service.users().messages()
        message = msgs_service.get(userId=USER_ID, id=data["id"]).execute()
        print(message["payload"])

if __name__ == "__main__":
    main()
