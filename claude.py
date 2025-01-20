import boto3
import json

prompt_data ="""Human:Act as shakespear and write a poem on machine learning\n Assistant:"""
bedrock = boto3.client(service_name= 'bedrock-runtime')
payload = {
    "prompt": prompt_data,
    "max_tokens_to_sample": 4000,
    "temperature": 0.5,
    "top_p": 0.9,
    "top_k": 3,
    "stop_sequences": [ "Human: "],
    "anthropic_version": "bedrock-2023-05-31"  # Update this to the desired version of Bedrock Runtime
}

body = json.dumps(payload)

model_id ="anthropic.claude-v2:1"
response = bedrock.invoke_model(
    body=body,
    modelId=model_id,
    contentType= "application/json",
    accept = "*/*"
    )
respone = json.loads(response.get('body').read())
print(respone.get('completion'))


