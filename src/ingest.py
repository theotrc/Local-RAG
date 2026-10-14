import hashlib

from config import (
    DOCUMENTS_DIR,
    CHUNK_SIZE,
    CHUNK_OVERLAP
)

from loaders import load_all_documents
from chunker import chunk_text
from embeddings import EmbeddingModel
from database import VectorDatabase


def make_id(source: str, chunk_index: int):
    value = f"{source}:{chunk_index}"

    return hashlib.sha256(
        value.encode("utf-8")
    ).hexdigest()


def ingest():

    documents = load_all_documents(DOCUMENTS_DIR)

    print(f"{len(documents)} document(s) trouvé(s).")

    embedding_model = EmbeddingModel()
    database = VectorDatabase()

    all_chunks = []
    all_ids = []
    all_metadata = []

    for document in documents:

        chunks = chunk_text(
            document["text"],
            chunk_size=CHUNK_SIZE,
            overlap=CHUNK_OVERLAP
        )

        for index, chunk in enumerate(chunks):

            all_chunks.append(chunk)

            all_ids.append(
                make_id(
                    document["source"],
                    index
                )
            )

            all_metadata.append({
                "source": document["source"],
                "chunk": index
            })

    print(f"{len(all_chunks)} chunks générés.")

    embeddings = embedding_model.embed_documents(
        all_chunks
    )

    database.add_documents(
        ids=all_ids,
        documents=all_chunks,
        metadatas=all_metadata,
        embeddings=embeddings
    )

    print(
        f"Indexation terminée. "
        f"{database.count()} chunks dans Chroma."
    )


if __name__ == "__main__":
    ingest()