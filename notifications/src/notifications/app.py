import boto3


def handler(event, context):
    print(event)

    client = boto3.client('ses')
    response = client.send_email(
        Source='noreply@foodie2ue.com',
        Destination={
            'ToAddresses': ['brianz@gmail.com', ],
            'CcAddresses': [],
            'BccAddresses': []
        },
        Message={
            'Subject': {
                'Data': 'This is a test from Lambda/SES',
            },
            'Body':
                {
                    'Text': {
                        'Data': 'Hello! This is a test from Lambda/SES',
                    },
                    'Html': {
                        'Data': 'Hello! This is a test from Lambda/SES',
                    }
                }
        },
    )
    print(response)
