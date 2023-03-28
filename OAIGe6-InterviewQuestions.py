import openai
import json

# open the JSON file
with open('GPT-3-SECRET-KEY.json') as f:
    key = json.load(f)

# extract the API key from the JSON data
api_key = key['OPENAI_API_KEY']

#setting engine, prompt and other parameters
response = openai.Completion.create(
  engine="davinci-instruct-beta",
  prompt="Write a creative ad for the following product to run on Instagram:\n\"\"\"\"\"\"\nXR350 motorcycle for "
         "offroad and mountain riders. High performance 349cc engine. Available in 3 color segments. Customization "
         "available.\n\"\"\"\"\"\"\nThis is the ad I wrote for Instagram aimed at motorbiking lovers:\n\"\"\"\"\"\"",
  temperature=0.8,
  max_tokens=150,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0,
  stop=["\"\"\"\"\"\""]
)

#Printing the result
print(response['choices'][0]["text"])