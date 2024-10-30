import boto3

def lambda_handler(event, context):
    # Initialize the Textract client
    textract_client = boto3.client('textract')
    
    # Get the bucket name and the object key from the event
    bucket_name = event['bucket_name']
    object_key = event['key']
    
    # Call Amazon Textract to analyze the image
    response = textract_client.analyze_id(
        DocumentPages=[
            {
                'S3Object': {
                    'Bucket': bucket_name,
                    'Name': object_key,
                }
            },
        ]
    )
    
    # Parse the extracted text for details from the ID card
    id_details = parse_id_details(response)
    
    return {
        'statusCode': 200,
        'body': id_details
    }

def parse_id_details(textract_response):
    id_details = {}
    for document in textract_response.get('IdentityDocuments', []):
        for field in document.get('IdentityDocumentFields', []):
            field_type = field['Type']['Text']
            field_value = field['ValueDetection']['Text']
            id_details[field_type] = field_value

    return id_details