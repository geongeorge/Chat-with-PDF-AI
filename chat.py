import chromadb
from utils.api import chat
from decouple import config

question = "How will naval kill his grandmother using leverage?"

api_key = config("API_KEY")

chroma_client = chromadb.PersistentClient(path="./db")
collection = chroma_client.get_collection(name="naval")

result = collection.query(query_texts=[question], n_results=3)
# print(result["documents"])
resultStr = result["documents"][0]

prompt = f"""You are a helpful AI assitant. You need to provide a response to a question asked by a user.
Here are some context from the book navals almanak you will use to generate a response:
{resultStr}
The user asks: "{question}" You respond:"""

chat_result = chat(prompt, api_key)

print(chat_result)