import os
import boto3
from botocore.config import Config



session = boto3.Session(
    profile_name="sandbox",
    region_name="us-east-1"
)

s3 = session.client(
    "s3",
    config=Config(signature_version="s3v4"),
    verify=False #bypasses SSL certificate verification
)


#basically to download the files
# for i in range(1, 13):
#     key = f"file{i}.json"
#     s3.download_file("amzn-12-file", key, key)

for file in os.listdir("reports"):
    local_path = f"reports/{file}"
    s3_key = f"reports/{file}"

    s3.upload_file(local_path, "amzn-12-file", s3_key)



