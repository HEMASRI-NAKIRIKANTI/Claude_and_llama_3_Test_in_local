import boto3
import json

prompt_data ="""
 Act as shakespear and write a poem on machine learning
"""
bedrock = boto3.client(service_name= 'bedrock-runtime')
payload = {
    "prompt": prompt_data,
    "max_gen_len": 512,
    "temperature": 0.5,
    "top_p": 0.9
}

body = json.dumps(payload)

model_id ="meta.llama3-8b-instruct-v1:0"
response = bedrock.invoke_model(
    body=body,
    modelId=model_id,
    contentType= "application/json",
    accept = "application/json"
    )
respone = json.loads(response.get('body').read())
poem = respone['generation']
print(poem)
