import os
import json

from foodie2ue.powertools import (
    EventBridgeEvent,
    LambdaContext,
    event_source,
    logger,
)

DEBUG = json.loads(os.environ.get('DEBUG', 'true'))


@event_source(data_class=EventBridgeEvent)
def handle_driver_dispatch(event: EventBridgeEvent, context: LambdaContext) -> None:
    status = event.detail.get('status')

    logger.info({'action': 'NOTIFY', 'type': event.detail_type, 'status': status})
