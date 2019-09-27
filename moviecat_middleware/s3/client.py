
import boto3
from ..settings import S3_BUCKET_NAME

class BucketClient:

    
    def __init__(self):
        self._s3 = boto3.resource('s3')
        self._bucket = self._s3.Bucket(S3_BUCKET_NAME)


    def upload_image(self, name, data):
        return self._bucket.put_object(Key='test.jpg', Body=data)


bucket = BucketClient()
