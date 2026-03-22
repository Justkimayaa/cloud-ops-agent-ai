import boto3
import json
import os
from datetime import datetime
from uuid import uuid4
from dotenv import load_dotenv

load_dotenv()

S3_BUCKET = os.getenv("S3_AUDIT_BUCKET")
AWS_REGION = os.getenv("AWS_REGION")

def log_decision(observation, reasoning, action, outcome):
    """Log every agent decision to AWS S3"""
    try:
        entry = {
            "timestamp": datetime.now().isoformat(),
            "observation": observation,
            "reasoning": reasoning,
            "action": action,
            "outcome": outcome
        }
        
        s3 = boto3.client('s3', region_name=AWS_REGION)
        key = f"logs/{datetime.now().strftime('%Y-%m-%d')}/{uuid4()}.json"
        
        s3.put_object(
            Bucket=S3_BUCKET,
            Key=key,
            Body=json.dumps(entry, indent=2)
        )
        print(f"Decision logged to S3: {key}")
        return True
    except Exception as e:
        print(f"Error logging to S3: {str(e)}")
        local_log(entry)
        return False

def local_log(entry):
    """Fallback — save log locally if S3 fails"""
    try:
        os.makedirs("logs", exist_ok=True)
        filename = f"logs/{uuid4()}.json"
        with open(filename, 'w') as f:
            json.dump(entry, f, indent=2)
        print(f"Decision logged locally: {filename}")
    except Exception as e:
        print(f"Error logging locally: {str(e)}")
