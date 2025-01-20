# {
#  "modelId": "stability.stable-diffusion-xl-v1",
#  "contentType": "application/json",
#  "accept": "application/json",
#  "body": "{\"text_prompts\":[{\"text\":\"this is where you place your input text\",\"weight\":1}],\"cfg_scale\":10,\"seed\":0,\"steps\":50,\"width\":512,\"height\":512}"
# }
import boto3
import json
import base64

promp_data = """{
 "text_prompts":
  [
    {
      "text": "A beautiful sunset over a serene lake in a magical forest setting.",
      "weight": 1
    }
  ],
  "cfg_scale": 10,
  "seed": 0,
  "steps": 50,
  "width": 512,
  "height": 512 
  }
"""
boto3_client = boto3.client(service_name='bedrock-runtime')
payload ={
    "modelId": "stability.stable-diffusion-xl-v1",
    "contentType": "application/json",
    "accept": "application/json",
    "body":promp_data
}


respone = boto3_client.invoke_model(
  **payload
)
response_body = json.loads(respone.get("body").read())
print(response_body['result'])

base64_image = response_body.get("artifacts")[0].get("base64")
base64_bytes = base64_image.encode('ascii')
image_bytes = base64.b64decode(base64_bytes)

with open('output.png', 'wb') as f:
    f.write(image_bytes)