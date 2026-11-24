# 📚 Document Assistant Using Retrieval-Augmented Generation (RAG)

An AI-powered Document Question Answering Assistant that allows users to upload PDF documents and ask questions in natural language. The application uses Retrieval-Augmented Generation (RAG) to retrieve relevant information from uploaded documents and generate context-based answers using an LLM.

## 🚀 Project Overview

The Document Assistant simplifies document analysis by allowing users to interact with PDF files through a conversational interface.

Instead of manually searching through lengthy documents, users can ask questions and receive relevant answers with source references, including document names and page numbers.

The application combines semantic search, vector embeddings, and Large Language Models (LLMs) to provide document-grounded responses.

## ✨ Features

- **Multiple PDF Upload:** Upload and process multiple PDF documents.
- **PDF Text Extraction:** Extract text from PDF files using PyMuPDF.
- **Intelligent Text Chunking:** Split extracted content into smaller, meaningful passages.
- **Embedding Generation:** Generate semantic embeddings using HuggingFace Sentence Transformers.
- **Vector Storage:** Store and index embeddings using FAISS.
- **Semantic Search:** Retrieve relevant document passages based on user questions.
- **AI-Powered Answers:** Generate contextual responses using Groq LLM.
- **Source Citations:** Display document names, page numbers, and chunk references.
- **Conversation History:** Maintain previous questions and answers during the session.
- **Document Management:** Clear uploaded document indexes and process new files.
- **Error Handling:** Handle empty PDFs, unreadable documents, and unsupported files.

## 🛠️ Technology Stack

| Technology                        | Purpose                               |
| --------------------------------- | ------------------------------------- |
| Python                            | Backend programming                   |
| Streamlit                         | Interactive web interface             |
| LangChain                         | RAG workflow orchestration            |
| PyMuPDF                           | PDF text extraction                   |
| RecursiveCharacterTextSplitter    | Text chunking                         |
| HuggingFace Sentence Transformers | Text embeddings                       |
| all-MiniLM-L6-v2                  | Embedding model                       |
| FAISS                             | Vector database and similarity search |
| Groq API                          | LLM inference                         |
| python-dotenv                     | Environment variable management       |
| Git & GitHub                      | Version control                       |

## 🏗️ Project Architecture

The application follows a modular Retrieval-Augmented Generation architecture.

### RAG Workflow

```text
             User
               |
               v
       Upload PDF Documents
               |
               v
        PDF Text Extraction
             (PyMuPDF)
               |
               v
         Text Chunking
    (Recursive Character Splitter)
               |
               v
       Embedding Generation
    (all-MiniLM-L6-v2)
               |
               v
         FAISS Vector Store
               |
               |
        User Asks Question
               |
               v
       Query Embedding
               |
               v
        Semantic Retrieval
               |
               v
      Retrieve Top-K Chunks
               |
               v
        Context Construction
               |
               v
         Groq LLM
               |
               v
       Grounded Answer
               |
               v
       Source References
```

## 📂 Project Structure

```text
document-assistant-rag/
│
├── app.py
├── requirements.txt
├── .env
├── .gitignore
├── README.md
│
├── src/
│   ├── __init__.py
│   ├── pdf_processor.py
│   ├── text_splitter.py
│   ├── embeddings.py
│   ├── vector_store.py
│   └── rag_chain.py
│
└── utils/
    ├── __init__.py
    └── prompts.py
```

## ⚙️ RAG Implementation Details

### 1. Document Ingestion

PyMuPDF extracts text from uploaded PDF documents page by page.

Each extracted page is stored as a LangChain Document containing:

- Page content
- Source document name
- Page number

Empty or unreadable PDFs are handled with informative error messages.

### 2. Text Chunking

The extracted text is divided into smaller passages using LangChain's RecursiveCharacterTextSplitter.

**Configuration:**

| Parameter       |           Value |
| --------------- | --------------: |
| Chunk Size      | 1000 characters |
| Chunk Overlap   |  200 characters |
| Top-K Retrieval |               4 |

**Why these values?**

- A chunk size of 1000 characters provides sufficient context for semantic retrieval.
- A 200-character overlap preserves contextual continuity between neighboring chunks.
- Retrieving four chunks provides multiple relevant passages without unnecessarily increasing the LLM context.

These parameters can be adjusted depending on document length and retrieval quality.

### 3. Embedding Generation

The application uses the HuggingFace model:

`sentence-transformers/all-MiniLM-L6-v2`

The model converts text passages into 384-dimensional dense vector representations.

**Why this model?**

- Open-source and free to use.
- Lightweight compared with larger embedding models.
- Supports semantic similarity search.
- Runs locally without requiring a paid embedding API.

### 4. Vector Database

FAISS (Facebook AI Similarity Search) stores and indexes the generated embeddings.

When a user uploads and processes documents, a new FAISS index is created.

The application uses vector similarity search to retrieve the most relevant passages for a question.

### 5. Semantic Retrieval

When a user submits a question:

1. The question is converted into an embedding.
2. FAISS searches for the closest document vectors.
3. The top four matching chunks are retrieved.
4. Document names, page numbers, and chunk references are collected.
5. Retrieved passages are combined into a context for the LLM.

### 6. Grounded Answer Generation

Groq API is used to generate answers from the retrieved document context.

The system prompt instructs the LLM to:

- Answer strictly using retrieved context.
- Avoid inventing information.
- Avoid using external knowledge.
- Clearly state when the requested information is unavailable.
- Provide clear and structured responses.

Source metadata is retained to display document and page references alongside answers.

**Note:** Prompt instructions help reduce unsupported answers but do not guarantee complete hallucination prevention.

## 📦 Installation and Setup

### Prerequisites

- Python 3.10 or higher
- pip package manager
- Git
- Groq API key

### Step 1: Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Navigate to the project directory:

```bash
cd document-assistant-rag
```

### Step 2: Create a Virtual Environment

```bash
python -m venv .venv
```

Activate the environment.

**Linux / macOS:**

```bash
source .venv/bin/activate
```

**Windows:**

```bash
.venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Step 4: Configure Environment Variables

Create a `.env` file in the root directory.

```env
GROQ_API_KEY=your_groq_api_key
```

Get your API key from:

https://console.groq.com/keys

### Step 5: Run the Application

```bash
streamlit run app.py
```

The application will be available at:

http://localhost:8501

## 🧪 Testing

The following scenarios can be used to test the application:

| Test Case                         | Expected Result                    |
| --------------------------------- | ---------------------------------- |
| Upload a valid PDF                | Document processed successfully    |
| Upload multiple PDFs              | All documents indexed              |
| Upload an empty PDF               | Informative error message          |
| Upload a scanned PDF              | Message indicating OCR is required |
| Ask a question about the document | Relevant contextual answer         |
| Ask an unrelated question         | Unavailable-information response   |
| Clear documents                   | Existing vector index removed      |
| Clear conversation                | Chat history removed               |
| Upload new documents              | Previous vector index replaced     |

## 🌐 Deployment

The application can be deployed using Streamlit Community Cloud.

### Deployment Steps

1. Push the project source code to GitHub.
2. Visit https://share.streamlit.io/
3. Connect your GitHub account.
4. Select the project repository.
5. Set the main application file to `app.py`.
6. Add the Groq API key under Streamlit application secrets.

Add the following in Streamlit Secrets:

```toml
GROQ_API_KEY = "your_groq_api_key"
```

7. Deploy the application.

## ⚠️ Known Limitations

- Scanned PDFs are not supported because OCR functionality is not currently implemented.
- Password-protected PDFs cannot be processed.
- FAISS stores the vector index in memory, so it does not persist across application restarts.
- Large documents may require additional system memory and processing time.
- Internet connectivity is required for Groq API inference.
- Retrieval quality depends on document quality, chunking, and embedding performance.
- The LLM may occasionally generate unsupported information despite context-grounding instructions.

## 🔮 Future Enhancements

- Add OCR support for scanned PDF documents.
- Implement persistent vector storage using ChromaDB.
- Add user authentication and document-level access control.
- Support DOCX and TXT documents.
- Implement hybrid search combining keyword and semantic retrieval.
- Add document summarization.
- Improve retrieval using reranking techniques.
- Add automated retrieval and answer-quality evaluation.

## 👩‍💻 Author

**Priyanka Raju Mohole**

GitHub: https://github.com/priyankamohole

## 📄 License

This project is developed
