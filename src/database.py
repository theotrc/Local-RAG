import chromadb

from config import CHROMA_DIR, COLLECTION_NAME


class VectorDatabase:

    def __init__(self):
        self.client = chromadb.PersistentClient(
            path=str(CHROMA_DIR)
        )

        self.collection = self.client.get_or_create_collection(
            name=COLLECTION_NAME,
            metadata={
                "hnsw:space": "cosine"
            }
        )

    def add_documents(
        self,
        ids,
        documents,
        metadatas,
        embeddings
    ):
        self.collection.add(
            ids=ids,
            documents=documents,
            metadatas=metadatas,
            embeddings=embeddings
        )

    def search(self, embedding, top_k=5):
        return self.collection.query(
            query_embeddings=[embedding],
            n_results=top_k
        )

    def count(self):
        return self.collection.count()