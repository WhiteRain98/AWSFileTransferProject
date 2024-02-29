import os
import boto3
from botocore.exceptions import ClientError

access_key = 'AKIA4UAUYC5I44DQROH5'
access_secret = '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'
bucketName = 'aaryansuploadedfiles'

"""
Connect to S3 service
"""

client_s3 = boto3.client(
    's3',
    aws_access_key_id = access_key,
    aws_secret_access_key = access_secret
)

"""
Upload files to S3 bucket
"""
data_file_folder = '/Users/aaryangupta/Desktop/TransferFolder'
for file in os.listdir(data_file_folder):
    if not file.startswith('~'):
        try:
            print('Uploading file {0}...'.format(file))
            client_s3.upload_file(
                os.path.join(data_file_folder, file),
                bucketName,
                file
            )
        except ClientError as e:
            print('Credential is incorrect')
            print(e)
        except Exception as e:
            print(e)