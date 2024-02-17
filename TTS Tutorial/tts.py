# Import packages
import requests
from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize variables and constants
CHUNK_SIZE = 1024
openai_client = OpenAI()
xi_key = os.getenv('XI-KEY')
voice_id = "zpnRoleXRhWcv8KmQc0N" # You can choose any voice ID. You might not have access to this one, keep in mind.
url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"

# Be as specific as possible in the 'system' role prompts.
completion_messages = [{"role": "system",
                        "content": "Create a short form video script in the style of a short-form video influencer. Keep the script under 100 words and do not include script prompts."}]

# User input
prompt = input("Enter the topic of your voiceover: ")
completion_messages.append({"role": "user",
                           "content": prompt})


# Create completion
completion = openai_client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=completion_messages,
    temperature=0.7
)

# Track completion as 'assistant' response.
completion_messages.append({"role": "assistant",
                           "content": completion.choices[0].message.content})

# Headers for API call.
headers = {
  "Accept": "audio/mpeg",
  "Content-Type": "application/json",
  "xi-api-key": xi_key
}

# Body data for API call.
data = {
  "text": completion.choices[0].message.content,
  "model_id": "eleven_monolingual_v1",
  "voice_settings": {
    "stability": 0.5,
    "similarity_boost": 0.5
  }
}

# Send POST request to Elevan Labs API. 
response = requests.post(url, json=data, headers=headers)

# Create the output.mp3 file. 
with open('output.mp3', 'wb') as f:
    for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
        if chunk:
            f.write(chunk)