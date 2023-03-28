import os
import openai
import APIKeyImporter


openai.api_key = APIKeyImporter.getKey()
print(openai.api_key)

# from gpt import GPT
# from gpt import Example
# gpt = GPT(engine="davinci",
#           temperature=0.5,
#           max_tokens=100)

#Adding Examples for GPT-3 model
#Example1
# gpt.add_example(Example('Find unique values of DEPARTMENT from Employee table.',
#                         'Select distinct DEPARTMENT from Employee;'))
#
# #Example2
# gpt.add_example(Example("Find the count of employees in department ECE.",
#                         "SELECT COUNT(*) FROM Employee WHERE DEPARTMENT = 'ECE';"))

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="### Postgres SQL tables, with their properties:\n#\n# Employee(id, name, department_id)\n# Department(id, name, address)\n# Salary_Payments(id, employee_id, amount, date)\n#\n### A query to list the names of the departments which employed more than 10 employees in the last 3 months\nSELECT",
  temperature=0,
  max_tokens=150,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0,
  stop=["#", ";"]
)

print(response.choices[0].text)
