import os
from langchain_openai import OpenAIEmbeddings
import weaviate
from langchain_weaviate.vectorstores import WeaviateVectorStore

embeddings = OpenAIEmbeddings(openai_api_key=os.getenv('OPENAI_API_KEY'), model="text-embedding-ada-002")

def persists(docs):
    weaviate_client = weaviate.connect_to_local()
    try:
        WeaviateVectorStore.from_documents(docs, embeddings, client=weaviate_client)
    finally:
        weaviate_client.close()