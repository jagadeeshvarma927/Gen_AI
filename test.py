# from config.config_loader import load_config

# config=load_config()

# collection_name = config["astra_db"]["collection_name"]
# embedding_model_name = config["embedding_model"]["model_name"]
# top_k = config["retriever"]["top_k"]

# print(collection_name)
# print(embedding_model_name)
# print(top_k)

# To run this code you need to install the following dependencies:
# pip install google-genai

import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI

def test_google_api_key():
    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY")
    print("Loaded GOOGLE_API_KEY:", api_key[:8] + "..." if api_key else "None")

    # Test Embedding
    try:
        embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")
        result = embeddings.embed_query("Test embedding for Gemini API key validation.")
        print("Embedding API key is valid. Sample embedding:", result[:5], "...")
    except Exception as e:
        print("Embedding API key is INVALID or not enabled for Gemini:", e)

    # Test Chat
    try:
        chat = ChatGoogleGenerativeAI(model="gemini-pro")
        response = chat.invoke("Say hello from Gemini!")
        print("Chat API key is valid. Gemini response:", response.content)
    except Exception as e:
        print("Chat API key is INVALID or not enabled for Gemini:", e)

if __name__ == "__main__":
    test_google_api_key()