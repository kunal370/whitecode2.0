import os
from sentence_transformers import SentenceTransformer
import chromadb
from dotenv import load_dotenv

load_dotenv()


def train():
    # Setup ChromaDB
    client = chromadb.PersistentClient(path="models/db")
    collection = client.get_or_create_collection("code_snippets")

    # Process all Python files
    code_pieces = []
    for root, _, files in os.walk("data"):
        for file in files:
            if file.endswith(".py"):
                try:
                    with open(os.path.join(root, file), "r", encoding="utf-8") as f:
                        code = f.read()
                        code_pieces.append(code)
                except UnicodeDecodeError:
                    print(f"Skipping {file} - could not read with UTF-8 encoding")
                    continue

    # Store in database
    if code_pieces:
        embeddings = SentenceTransformer('all-MiniLM-L6-v2').encode(code_pieces)
        collection.add(
            ids=[str(i) for i in range(len(code_pieces))],
            documents=code_pieces,
            embeddings=embeddings.tolist()
        )
        print(f"Trained on {len(code_pieces)} files")
    else:
        print("No valid Python files found in data/")


if __name__ == "__main__":
    if not os.path.exists("data"):
        os.makedirs("data")
    if not os.path.exists("models"):
        os.makedirs("models")
    train()