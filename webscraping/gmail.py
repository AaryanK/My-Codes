from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

SCOPES = ['https://mail.google.com/']

creds = None

if os.path.exists('tokens/gmail.pickle'):
        with open('tokens/gmail.pickle', 'rb') as token:
            creds = pickle.load(token)

if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())

        else:
            flow = InstalledAppFlow.from_client_secrets_file('gmail.json', SCOPES)
            creds = flow.run_local_server(port=0)

        with open('tokens/gmail.pickle', 'wb') as token:
            pickle.dump(creds, token)

service = build('gmail', 'v1', credentials=creds)

try:
    message = (service.users().messages().send(userId='grihakumar@gmail.com', body='hey')
                .execute())
    print ('Message Id: %s' % message['id'])
except Exception:
        print ('An error occurred: %s')