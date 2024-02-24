import requests
import json

def chat(prompt, key):
    if key is None:
        raise Exception("API key is required")
    else:
      response = requests.post(
            url='https://api.together.xyz/inference',
            headers={
                "Authorization": f"Bearer {key}",
                "Content-Type": "application/json"
            },                
            json={
                "model": "mistralai/Mixtral-8x7B-Instruct-v0.1",
                "prompt": f"[INST] {prompt} [/INST]",
                "max_tokens": 4096,
                "temperature": 0.7,
            },)

      if response.status_code == 200:
          content = response.json()
          return content["output"]["choices"][0]["text"]
      else:
          raise Exception(f"Request failed with status code {response.status_code}")
