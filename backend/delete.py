# import sqlite3

# conn = sqlite3.connect(r"D:\Practice\EXL\InsightBot\backend\chroma_db\chroma.sqlite3")
# cursor = conn.cursor()

# import chromadb

# client = chromadb.PersistentClient(path=r"D:\Practice\EXL\InsightBot\backend\chroma_db")

# collections = client.list_collections()
# print(collections)
# for c in collections:
#     print(c.name)




# import chromadb

# client = chromadb.PersistentClient(path="chroma_db")

# collection = client.get_collection("documents")

# data = collection.get(
#     include=["documents", "metadatas", "embeddings"]
# )

# print("Number of documents:", len(data["documents"]))

# # Print the first embedding vector
# print(data["embeddings"][0])    





import google.generativeai as genai

genai.configure(api_key="")

for model in genai.list_models():
    print(model.name)