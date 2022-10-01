from abc import ABC
from dataclasses import dataclass

import boto3


@dataclass()
class NotifierPayload():
    recipient: str
    html_body: str
    text_body: str
    from_email: str
    subject: str


class AbstractNotifier(ABC):

    def notify(self, payload: NotifierPayload) -> None:
        raise NotImplementedError


class SESNotifier(AbstractNotifier):

    def __enter__(self):
        self.__client = boto3.client('ses')

    def notify(self, payload: NotifierPayload) -> None:
        self.__client.send_email(
            Source=payload.from_email,
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
