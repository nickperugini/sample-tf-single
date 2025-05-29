import os
import boto3

def lambda_handler(event, context):
    s3 = boto3.client("s3")
    bucket = os.environ["BUCKET"]
    s3.put_object(Bucket=bucket, Key="test.txt", Body="Hello from Lambda!")
    return {"statusCode": 200, "body": "Uploaded to S3"}
