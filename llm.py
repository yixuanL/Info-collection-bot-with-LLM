import json
from langchain_openai import ChatOpenAI
# from langchain.vectorstores.weaviate import Weaviate
# from langchain.llms import OpenAI
import weaviate.classes as wvc
import weaviate

def get_keys(path):
    with open(path) as f:
        return json.load(f)

keys = get_keys(".secret/api_keys.json")

llm = ChatOpenAI(
    api_key = keys["OPENAI_API_KEY"]
)

# question = "Since when is LangChain available?"

# response = llm.invoke(question)

# print(response)

client = weaviate.connect_to_wcs(
    cluster_url=keys["WCS_URL"],
    auth_credentials=weaviate.auth.AuthApiKey(keys["WCS_KEY"]),
    headers={
        "X-OpenAI-Api-Key": keys["OPENAI_API_KEY"]
    }
)

try:
    # Your code here
    pass
except:
    # Close the connection gracefully
    client.close()