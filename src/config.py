from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

DOCUMENTS_DIR = BASE_DIR / "documents"
CHROMA_DIR = BASE_DIR / "data" / "chroma"

COLLECTION_NAME = "documents"

OLLAMA_URL = "http://localhost:11434"
LLM_MODEL = "llama3.1:8b"

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

CHUNK_SIZE = 800
CHUNK_OVERLAP = 150

TOP_K = 5