import os
import json

from notifications.powertools import (
    EventBridgeEvent,
    LambdaContext,
    event_source,
    logger,
)

from notifications.notifier import AbstractNotifier, SESNotifier, NotifierPayload
from notifications.renderer import render_new_order

DEBUG = json.loads(os.environ.get('DEBUG', 'true'))


# @logger.inject_lambda_context
@event_source(data_class=EventBridgeEvent)
def handle_notification(event: EventBridgeEvent, context: LambdaContext) -> None:
    recipient = event.detail.get('recipient')

    logger.info({'action': 'NOTIFY', 'type': event.detail_type, 'recipient': recipient})

    if not recipient:
        logger.error({'message': 'User not found in event payload', **event.detail})

    if DEBUG and recipient not in ('brianz@gmail.com', 'matt.d.diamond@hotmail.com'):
        recipient = 'brianz@gmail.com'

    text_body, html_body = render_new_order(event.detail)

    payload = NotifierPayload(
        recipient=recipient,
        text_body=text_body,
        html_body=html_body,
        subject='New order notification',
    )
    notifier: AbstractNotifier = SESNotifier()
    notifier.notify(payload)
