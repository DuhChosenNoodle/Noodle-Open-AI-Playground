import openai
import json

# open the JSON file
with open('GPT-3-SECRET-KEY.json') as f:
    key = json.load(f)

# extract the API key from the JSON data
openai.api_key = key['OPENAI_API_KEY']

# Prompt GPT3 to generate a recipe
response = openai.Completion.create(
  engine="davinci-instruct-beta",
  prompt="Write a recipe based on these ingredients and instructions:\n\nCaramel Custard\n\nIngredients:\nMilk\nCustard Powder\n\nSugar\nMilkmaid\n\n Steps to be followed:",
  temperature=0,
  max_tokens=150,
  top_p=1.0,
  frequency_penalty=0.5,
  presence_penalty=0.5
)

#print(response)
print(response['choices'][0]["text"])