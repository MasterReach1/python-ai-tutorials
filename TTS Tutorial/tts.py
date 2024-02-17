import requests
import os
from dotenv import load_dotenv

load_dotenv()
CHUNK_SIZE = 1024
xi_key = os.getenv('XI-KEY')
voice_id = "zpnRoleXRhWcv8KmQc0N"
url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"

headers = {
  "Accept": "audio/mpeg",
  "Content-Type": "application/json",
  "xi-api-key": xi_key
}

data = {
  "text": "Like and subscribe if you're enjoying this.",
  "model_id": "eleven_monolingual_v1",
  "voice_settings": {
    "stability": 0.5,
    "similarity_boost": 0.5
  }
}

response = requests.post(url, json=data, headers=headers)

with open('output.mp3', 'wb') as f:
    for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
        if chunk:
            f.write(chunk)