import json
import boto3
import base64
import uuid

# Initialize DynamoDB client
dynamodb = boto3.client('dynamodb')

# Initialize S3 client
s3 = boto3.client('s3')

def lambda_handler(event, context):
    # Get the data from the event object
    data1 = json.dumps(event['body'])
    data = json.loads(data1)
    name = data['name']
    email = data.get('email', '')
    message = data['message']
    image = data['image']
    
    # Decode the base64 encoded image
    image_data = base64.b64decode(image)
    
    # Upload the image to the S3 bucket
    bucket_name = 'YOUR_BUCKET_NAME'
    s3.put_object(Body=image_data, Bucket=bucket_name, Key=name+'.jpg')
    
    # Add the data to the DynamoDB table
    table_name = 'YOUR_TABLE_NAME'
    id = str(uuid.uuid4())
    dynamodb.put_item(
        TableName=table_name,
        Item={
            'id': {'S': id},
            'name': {'S': name},
            'email': {'S': email},
            'message': {'S': message},
            'image_url': {'S': f's3://{bucket_name}/{name}.jpg'}
        }
    )
    
    # Return a response
    response = {
        'statusCode': 200,
        'body': json.dumps({'message': 'Data added successfully'})
    }
    
    return response
