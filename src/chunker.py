def chunk_text(
    text: str,
    chunk_size: int = 800,
    overlap: int = 150
):
    text = text.replace("\r\n", "\n").strip()

    chunks = []

    start = 0

    while start < len(text):
        end = start + chunk_size

        chunk = text[start:end].strip()

        if chunk:
            chunks.append(chunk)

        if end >= len(text):
            break

        start = end - overlap

    return chunks