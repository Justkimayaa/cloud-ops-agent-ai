import boto3
import os
from langchain.tools import tool
from dotenv import load_dotenv

load_dotenv()

SNS_TOPIC_ARN = os.getenv("SNS_TOPIC_ARN")
AWS_REGION = os.getenv("AWS_REGION")

@tool
def send_alert(message: str, severity: str) -> str:
    """Send incident alert via AWS SNS to email"""
    try:
        sns = boto3.client('sns', region_name=AWS_REGION)
        sns.publish(
            TopicArn=SNS_TOPIC_ARN,
            Message=message,
            Subject=f"[{severity}] Cloud Ops Agent Alert"
        )
        return f"Alert sent successfully with severity: {severity}"
    except Exception as e:
        return f"Error sending alert: {str(e)}"

@tool
def send_resolution(message: str) -> str:
    """Send resolution notification via AWS SNS"""
    try:
        sns = boto3.client('sns', region_name=AWS_REGION)
        sns.publish(
            TopicArn=SNS_TOPIC_ARN,
            Message=message,
            Subject="[RESOLVED] Cloud Ops Agent - Issue Fixed"
        )
        return "Resolution notification sent successfully"
    except Exception as e:
        return f"Error sending resolution: {str(e)}"
