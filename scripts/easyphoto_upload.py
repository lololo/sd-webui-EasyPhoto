import os
import boto3

from dotenv import load_dotenv
from scripts.easyphoto_config import lora_dir, env_path
load_dotenv(dotenv_path=env_path)

endpoint_url = os.getenv('endpoint_url')

s3 = boto3.client(
    service_name ="s3",
    endpoint_url = os.getenv('endpoint_url'),
    aws_access_key_id = os.getenv('aws_access_key_id'),
    aws_secret_access_key = os.getenv('aws_secret_access_key'),
    region_name=os.getenv('region_name') # Must be one of: wnam, enam, weur, eeur, apac, auto
)

def easyphoto_file_upload(user_id):
    lora_filename = user_id + ".safetensors"
    lora_filepath = os.path.join(lora_dir, lora_filename )
    print(lora_filename)
    print(lora_filepath)

    try:
        res = s3.upload_file(lora_filepath, 'loras', lora_filename)
    except Exception as e:
        print(e)
        raise e
        
    return res
    