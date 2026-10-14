from pathlib import Path
import fitz


def load_pdf(path: Path) -> str:
    text = []

    with fitz.open(path) as pdf:
        for page in pdf:
            text.append(page.get_text())

    return "\n".join(text)


def load_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def load_document(path: Path) -> str:
    suffix = path.suffix.lower()

    if suffix == ".pdf":
        return load_pdf(path)

    if suffix in {".txt", ".md"}:
        return load_text(path)

    raise ValueError(f"Format non supporté : {suffix}")


def load_all_documents(directory: Path):
    documents = []

    for path in directory.rglob("*"):
        if not path.is_file():
            continue

        if path.suffix.lower() not in {".pdf", ".txt", ".md"}:
            continue

        text = load_document(path)

        if text.strip():
            documents.append({
                "source": str(path),
                "text": text
            })

    return documents