# Document Assistant Using RAG

## Overview

Document Assistant is an AI-powered PDF question-answering
application built using Retrieval-Augmented Generation (RAG).

Users can upload PDF documents and ask questions in natural
language. The application retrieves relevant document passages
and uses an LLM to generate context-grounded answers.

## Technology Stack

- Python
- Streamlit
- LangChain
- PyMuPDF
- HuggingFace Sentence Transformers
- FAISS
- Groq LLM API

## Architecture

PDF Upload
|
v
PDF Text Extraction
|
v
Text Chunking
|
v
HuggingFace Embeddings
|
v
FAISS Vector Database
|
v
User Question
|
v
Semantic Search
|
v
Relevant Context Retrieval
|
v
Groq LLM
|
v
Grounded Answer + Citations

## Chunking Strategy

Chunk Size: 1000 characters
Chunk Overlap: 200 characters

RecursiveCharacterTextSplitter is used to preserve
logical text boundaries and maintain contextual continuity.

## Embedding Model

Model: sentence-transformers/all-MiniLM-L6-v2

This model generates 384-dimensional embeddings.
It is lightweight, open-source, and runs locally.

## Vector Database

FAISS is used for efficient vector similarity search.
The vector index is created in memory and refreshed
when new documents are processed.

## LLM

Groq API is used for answer generation.

Temperature is set to 0 to encourage consistent,
focused responses.

## Installation

1. Clone the repository.

git clone YOUR_GITHUB_REPOSITORY_URL

2. Navigate to the project.

cd document-assistant-rag

3. Create a virtual environment.

python -m venv .venv

4. Activate the environment.

source .venv/bin/activate

5. Install dependencies.

pip install -r requirements.txt

6. Create a .env file.

GROQ_API_KEY=your_api_key

7. Run the application.

streamlit run app.py

## Features

- Multiple PDF uploads
- PDF text extraction
- Automatic text chunking
- Local embedding generation
- FAISS vector indexing
- Semantic document retrieval
- LLM-powered question answering
- Source citations with page numbers
- Conversation history
- Document and chat clearing
- Scanned PDF detection

## Limitations

- Scanned PDFs require OCR.
- Internet access is required for Groq API calls.
- The FAISS index is stored in memory.
- Very large documents may require additional memory.
- Retrieval quality depends on chunking and embedding quality.
- The LLM may still make mistakes despite grounding instructions.

## Future Improvements

- OCR support using Tesseract.
- Persistent vector storage using ChromaDB.
- User authentication.
- Document summarization.
- Hybrid search using keyword and vector retrieval.
- Support for DOCX and TXT files.
- Multi-user document management.

## License

MIT License
