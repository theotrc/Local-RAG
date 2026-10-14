from retriever import Retriever
from llm import generate


SYSTEM_INSTRUCTION = """
Tu es un assistant spécialisé dans la réponse à partir
de documents fournis par l'utilisateur.

Règles :

1. Utilise uniquement les informations présentes dans le contexte.
2. Ne fabrique aucune information.
3. Si la réponse n'est pas présente dans le contexte,
   indique clairement que tu ne trouves pas la réponse.
4. Cite les sources utilisées lorsque c'est possible.
5. Réponds en français.
"""


class RAG:

    def __init__(self):
        self.retriever = Retriever()

    def answer(self, question):

        results = self.retriever.retrieve(question)

        context_parts = []

        for i, result in enumerate(results):

            context_parts.append(
                f"""
--- SOURCE {i + 1} ---
Fichier : {result["source"]}
Chunk : {result["chunk"]}

{result["text"]}
"""
            )

        context = "\n".join(context_parts)

        prompt = f"""
{SYSTEM_INSTRUCTION}

CONTEXTE :

{context}

QUESTION :

{question}

RÉPONSE :
"""

        answer = generate(prompt)

        return {
            "answer": answer,
            "sources": results
        }


if __name__ == "__main__":

    rag = RAG()

    while True:

        question = input("\nQuestion : ")

        if question.lower() in {
            "exit",
            "quit",
            "q"
        }:
            break

        result = rag.answer(question)

        print("\n" + result["answer"])

        print("\nSources :")

        for source in result["sources"]:
            print(
                f"- {source['source']} "
                f"(chunk {source['chunk']})"
            )