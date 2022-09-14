from multiprocessing import Event
import boto3

from jinja2 import Environment, FileSystemLoader, select_autoescape

from notifications.powertools import (
    EventBridgeEvent,
    LambdaContext,
    event_source,
    logger,
)

env = Environment(
    loader=FileSystemLoader("notifications/templates"),
    autoescape=select_autoescape(),
)


# @logger.inject_lambda_context
@event_source(data_class=EventBridgeEvent)
def handle_notification(event: EventBridgeEvent, context: LambdaContext) -> None:
    client = boto3.client('ses')

    recipient = event.detail.get('recipient')

    logger.info({'action': 'NOTIFY', 'type': event.detail_type, 'recipient': recipient})

    if not recipient:
        logger.error({'message': 'User not found in event payload', **event.detail})

    if recipient not in ('brianz@gmail.com', 'matt.d.diamond@hotmail.com'):
        recipient = 'brianz@gmail.com'

    html_template = env.get_template("order-email.html.j2")
    txt_template = env.get_template("order-email.txt.j2")

    client.send_email(
        Source='noreply@foodie2ue.com',
        Destination={
            'ToAddresses': [recipient], 'CcAddresses': [], 'BccAddresses': []
        },
        Message={
            'Subject': {
                'Data': "Thanks for your order!"
            },
            'Body': {
                'Text': {
                    'Data': txt_template.render(**event.detail)
                },
                'Html': {
                    'Data': html_template.render(**event.detail)
                }
            }
        },
    )


# logger.info(response)
