import os
import openai
import json

# openai.api_key = os.getenv("OPENAI_API_KEY")

# open the JSON file
with open('GPT-3-SECRET-KEY.json') as f:
    key = json.load(f)

# extract the API key from the JSON data
api_key = key['OPENAI_API_KEY']

from gpt import GPT
from gpt import Example
gpt = GPT(engine="davinci",
          temperature=0.5,
          max_tokens=100)

#Adding Examples for GPT-3 model
#Example1
gpt.add_example(Example('Find unique values of DEPARTMENT from Employee table.', 
                        'Select distinct DEPARTMENT from Employee;'))

#Example2
gpt.add_example(Example("Find the count of employees in department ECE.", 
                        "SELECT COUNT(*) FROM Employee WHERE DEPARTMENT = 'ECE';"))