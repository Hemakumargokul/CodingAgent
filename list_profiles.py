"""
Lists available AWS Bedrock inference profiles.
"""
import boto3
import json
from botocore.exceptions import ClientError

def list_inference_profiles():
    try:
        bedrock_client = boto3.client("bedrock", region_name="us-east-1")
        response = bedrock_client.list_inference_profiles()
        
        profiles = response.get("inferenceProfileSummaries", [])
        print(f"Found {len(profiles)} inference profiles:\n")
        
        for profile in profiles:
            print(f"Profile Name: {profile['inferenceProfileName']}")
            print(f"Profile ARN: {profile['inferenceProfileArn']}")
            print(f"Status: {profile['status']}")
            print(f"Type: {profile['type']}")
            if 'models' in profile:
                print(f"Models: {profile['models']}")
            print("-" * 50)
            
    except ClientError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    list_inference_profiles()


