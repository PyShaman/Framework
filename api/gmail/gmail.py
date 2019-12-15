import time
import base64
import colorama
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

SCOPES = 'https://www.googleapis.com/auth/gmail.modify'
colorama.init()


class MailListener:

    def __init__(self):
        pass

    @staticmethod
    def get_messages_and_service():
        store = file.Storage('token.json')
        creds = store.get()
        if not creds or creds.invalid:
            flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
            creds = tools.run_flow(flow, store)
        service = build('gmail', 'v1', http=creds.authorize(Http()))
        results = service.users().messages().list(userId='me', labelIds=['UNREAD']).execute()
        return [results.get('messages', []), service]

    def get_mail_text(self):
        messages = self.get_messages_and_service()[0]
        service = self.get_messages_and_service()[1]
        timeout = time.time() + 60
        while not messages:
            time.sleep(5)
            results = service.users().messages().list(userId='me', labelIds=['UNREAD']).execute()
            messages = results.get('messages', [])
            if messages or time.time() > timeout:
                break
        for message in messages:
            msg = service.users().messages().get(userId='me', id=message['id']).execute()
            payload = msg['payload']  # get payload of the message
            part_body = payload['body']  # fetching body of the message
            part_data = part_body['data']  # fetching data from the body
            clean_one = part_data.replace("-", "+")  # decoding from Base64 to UTF-8
            clean_one = clean_one.replace("_", "/")  # decoding from Base64 to UTF-8
            clean_two = base64.b64decode(bytes(clean_one, 'UTF-8')).decode('UTF-8')  # decoding from Base64 to UTF-8
            return clean_two

    def mark_message_as_read(self):
        messages = self.get_messages_and_service()[0]
        service = self.get_messages_and_service()[1]
        for message in messages:
            service.users() \
                .messages() \
                .modify(userId='me', id=message['id'], body={'removeLabelIds': ['UNREAD']}) \
                .execute()
