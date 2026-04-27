from sentence_transformers import SentenceTransformer
import chromadb
import re

model = SentenceTransformer('all-MiniLM-L6-v2')

client = chromadb.Client()
collection = client.get_or_create_collection(name="controls")


def load_documents(file_path):
    with open(file_path, "r") as f:
        return f.read()

def chunk_text(text, chunk_size=200, overlap=50):
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]

        if chunk.strip():
            chunks.append(chunk.strip())

        start += (chunk_size - overlap)

    return chunks

def store_embeddings(chunks):
    global collection

    try:
        client.delete_collection(name="controls")
    except:
        pass

    collection = client.get_or_create_collection(name="controls")

    embeddings = model.encode(chunks)

    for i, chunk in enumerate(chunks):
        collection.add(
            documents=[chunk],
            embeddings=[embeddings[i].tolist()],
            ids=[f"id_{i}"]
        )


def run_rag_pipeline():
    text = load_documents("data/controls.txt")
    chunks = chunk_text(text, chunk_size=100, overlap=20)
    store_embeddings(chunks)
    print("RAG pipeline completed. Stored", len(chunks), "chunks.")

def retrieve(query, top_k=2):
    query_embedding = model.encode([query])[0]

    results = collection.query(
        query_embeddings=[query_embedding.tolist()],
        n_results=top_k
    )

    return results["documents"][0]