import json
from langchain_openai import ChatOpenAI

def get_keys(path):
    with open(path) as f:
        return json.load(f)

keys = get_keys(".secret/api_keys.json")

llm = ChatOpenAI(
    api_key = keys["OPENAI_API_Key"]
)

response = llm.invoke("Since when is LangChain available?")

print(response)