from config import TOP_K

from embeddings import EmbeddingModel
from database import VectorDatabase


class Retriever:

    def __init__(self):
        self.embedding_model = EmbeddingModel()
        self.database = VectorDatabase()

    def retrieve(self, question, top_k=TOP_K):

        embedding = self.embedding_model.embed_query(
            question
        )

        results = self.database.search(
            embedding,
            top_k
        )

        documents = results["documents"][0]
        metadatas = results["metadatas"][0]
        distances = results["distances"][0]

        output = []

        for document, metadata, distance in zip(
            documents,
            metadatas,
            distances
        ):
            output.append({
                "text": document,
                "source": metadata["source"],
                "chunk": metadata["chunk"],
                "distance": distance
            })

        return output