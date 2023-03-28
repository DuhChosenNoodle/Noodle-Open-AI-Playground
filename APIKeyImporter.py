import json

# variables
api_key = "key"
filename = "GPT-3-SECRET-KEY"


def getKey():
    # open the JSON file
    with open(filename + '.json') as f:
        key = json.load(f)

    # extract the API key from the JSON data
    api_key = key['OPENAI_API_KEY']

    # print
    return api_key

# key = APIKeyImporter()
# print(key.getKey())
