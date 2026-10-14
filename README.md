# Local AI Agent

Ce projet est une application de recherche d'informations locale basée sur un pipeline RAG (Retrieval-Augmented Generation).

Il permet de :

- charger des fichiers PDF, TXT et MD depuis un dossier local,
- découper les documents en chunks,
- générer des embeddings à l’aide de sentence-transformers,
- stocker les embeddings dans ChromaDB,
- retrouver les meilleurs morceaux de texte selon une question,
- générer une réponse avec un modèle LLM local via Ollama.

## Architecture

Le projet est organisé de la manière suivante :

- `src/config.py` : configuration globale du projet (chemins, modèle d’embedding, modèle LLM, taille des chunks, etc.)
- `src/loaders.py` : chargement des documents depuis le dossier `documents`
- `src/chunker.py` : découpe des textes en morceaux
- `src/embeddings.py` : génération des embeddings avec Sentence Transformers
- `src/database.py` : gestion de la base vectorielle ChromaDB
- `src/retriever.py` : recherche des chunks les plus pertinents
- `src/llm.py` : appel au modèle local Ollama
- `src/ingest.py` : indexation des documents dans Chroma
- `src/rag.py` : pipeline complet de question/réponse

## Prérequis

Avant de lancer le projet, il faut installer :

- Python 3.10+
- Ollama
- Un modèle LLM compatible avec Ollama (par défaut : `llama3.1:8b`)

## Installation

1. Cloner le projet

```bash
git clone <url-du-projet>
cd Local AI AGENT
```

2. Créer un environnement virtuel et installer les dépendances

```bash
python -m venv .venv
source .venv/bin/activate
```

Sur Windows PowerShell :

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Puis :

```bash
pip install -r requirements.txt
```

3. Télécharger le modèle Ollama

```bash
ollama pull llama3.1:8b
```

4. Vérifier que Ollama tourne localement

Ollama est attendu sur :

```text
http://localhost:11434
```

## Préparer les documents

Placez vos fichiers dans le dossier `documents/` :

- fichiers `.pdf`
- fichiers `.txt`
- fichiers `.md`

Exemple :

```text
documents/
  rapport.pdf
  notes.md
  faq.txt
```

## Indexation des documents

Pour indexer les fichiers présents dans `documents/` dans ChromaDB :

```bash
python src/ingest.py
```

Cela va :

- lire les documents,
- les découper,
- générer les embeddings,
- les enregistrer dans la base vectorielle.

## Utilisation

Pour lancer le chatbot RAG en ligne de commande :

```bash
python src/rag.py
```

Ensuite, posez une question :

```text
Question : Quel est le sujet principal de ce document ?
```

Le système :

- recherche les chunks les plus proches de la question,
- construit un contexte enrichi,
- demande au modèle LLM de répondre à partir de ce contexte uniquement.

## Configuration

Le fichier `src/config.py` contient les paramètres principaux :

```python
DOCUMENTS_DIR = BASE_DIR / "documents"
CHROMA_DIR = BASE_DIR / "data" / "chroma"
COLLECTION_NAME = "documents"
OLLAMA_URL = "http://localhost:11434"
LLM_MODEL = "llama3.1:8b"
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
CHUNK_SIZE = 800
CHUNK_OVERLAP = 150
TOP_K = 5
```

Vous pouvez modifier ces valeurs selon votre environnement ou vos besoins.

## Données persistées

Le projet stocke :

- les embeddings et le vecteur store dans `data/chroma/`
- les documents sources dans `documents/`

## Limites

- Le système dépend de la disponibilité d’Ollama localement.
- Les réponses sont limitées aux contenus présents dans les documents ajoutés.
- La qualité des réponses dépend directement de la qualité des documents et du modèle choisi.

## Idée d’amélioration

Voici quelques pistes possibles :

- ajout d’une interface web avec Streamlit ou FastAPI,
- prise en charge de plus de formats de fichiers,
- ajout de métadonnées plus riches,
- nettoyage automatique des documents,
- gestion multi-utilisateurs / multi-collections.

## Licence

Ce projet est fourni sans licence spécifique. Vérifiez avant toute réutilisation commerciale ou publique.
