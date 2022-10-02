import os

from abc import ABC
from dataclasses import dataclass

import boto3

FROM_EMAIL = os.environ['DEFAULT_FROM_ADDRESS']


@dataclass()
class NotifierPayload():
    recipient: str
    html_body: str
    text_body: str
    subject: str
    # from_email: str


class AbstractNotifier(ABC):

    def notify(self, payload: NotifierPayload) -> None:
        raise NotImplementedError


class SESNotifier(AbstractNotifier):

    def __init__(self):
        self.__client = boto3.client('ses')

    def notify(self, payload: NotifierPayload) -> None:
        self.__client.send_email(
            Source=FROM_EMAIL,
            Destination={
                'ToAddresses': [payload.recipient],
                'CcAddresses': [],
                'BccAddresses': [],
            },
            Message={
                'Subject': {
                    'Data': payload.subject
                },
                'Body': {
                    'Text': {
                        'Data': payload.text_body
                    },
                    'Html': {
                        'Data': payload.html_body
                    },
                }
            },
        )
