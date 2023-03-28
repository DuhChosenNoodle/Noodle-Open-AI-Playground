import os
import openai
import json

# Load your API key from an environment variable or secret management service
# openai.api_key = os.getenv("OPENAI_API_KEY")
# open the JSON file
with open('GPT-3-SECRET-KEY.json') as f:
    data = json.load(f)

# extract the API key from the JSON data
api_key = data['OPENAI_API_KEY']

# use the API key in your program
print(api_key)

response = openai.Completion.create(engine="davinci", prompt="I saw a cat", max_tokens=50)
print(response)