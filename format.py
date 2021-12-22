import boto3
from fileinput import FileInput
from os import write

w = open("proxies.txt", "w")

with FileInput(files=['output.txt'], inplace=False) as f:
    for line in f:
        line = line.rstrip()
        line = "\'http://"+line+"\',"
        w.write(line+"\n")

w.close()

s3_client = boto3.client(
    's3',
    region_name='us-east-2',
    aws_access_key_id='AKIA2W2BDOC4HMOMPP6P',
    aws_secret_access_key='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',
)

with open("proxies.txt", "rb") as a:
    s3_client.upload_fileobj(a, "moxyproxy", "proxies.txt")

        