import openai
import json

# open the JSON file
with open('GPT-3-SECRET-KEY.json') as f:
    key = json.load(f)

# extract the API key from the JSON data
openai.api_key = key['OPENAI_API_KEY']

response = openai.Completion.create(
  engine="davinci",
  prompt="Create an outline for an essay about Metallica and their contribution to metal music:\n\nI: Introduction",
  temperature=0.7,
  max_tokens=150,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)

print(response['choices'][0]["text"])