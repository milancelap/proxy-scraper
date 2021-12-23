import boto3
import os
from fileinput import FileInput

w = open("proxies.txt", "w")

with FileInput(files=['output.txt'], inplace=False) as f:
    for line in f:
        line = line.rstrip()
        line = "\'http://"+line+"\',"
        w.write(line+"\n")

w.close()

ACCESS_KEY = os.environ.get('ACCESS_KEY')
SECRET_KEY = os.environ.get('SECRET_KEY')

s3_client = boto3.client(
    's3',
    region_name='us-east-2',
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY,
)

with open("proxies.txt", "rb") as a:
    s3_client.upload_fileobj(a, "moxyproxy", "proxies.txt", ExtraArgs={'ACL': 'public-read'})

        