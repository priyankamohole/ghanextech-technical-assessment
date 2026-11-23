
from langchain_groq import ChatGroq
from utils.prompts import RAG_PROMPT
import os


def get_llm():

    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise ValueError("GROQ_API_KEY is missing.")

    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0,
        api_key=api_key
    )

    return llm


def ask_question(vector_store, question):

    # Step 1: Retrieve relevant chunks
    results = vector_store.similarity_search_with_score(
        question,
        k=4
    )

    if not results:
        return "No relevant information found.", []

    # Step 2: Prepare context
    context_parts = []
    sources = []

    for document, score in results:

        source = document.metadata.get(
            "source", "Unknown document"
        )

        page = document.metadata.get(
            "page", "Unknown"
        )

        chunk_index = document.metadata.get(
            "chunk_index", "Unknown"
        )

        context_parts.append(
            f"""
            Source: {source}
            Page: {page}
            Chunk: {chunk_index}

            Content:
            {document.page_content}
            """
        )

        sources.append({
            "source": source,
            "page": page,
            "chunk": chunk_index
        })

    context = "\n\n".join(context_parts)

    # Step 3: Initialize LLM
    llm = get_llm()

    # Step 4: Construct prompt
    prompt = RAG_PROMPT.format(
        context=context,
        question=question
    )

    # Step 5: Generate grounded answer
    response = llm.invoke(prompt)

    # Step 6: Return answer and references
    unique_sources = []
    seen = set()

    for source in sources:
        key = (
            source["source"],
            source["page"],
            source["chunk"]
        )

        if key not in seen:
            seen.add(key)
            unique_sources.append(source)

    return response.content, unique_sources
