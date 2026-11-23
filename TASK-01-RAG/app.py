# import streamlit as st

# def main():
#     st.set_page_config(page_title="Ask about your DOCs", page_icon=":books:")
#     st.header("Ask about your DOCs :books:")
#     st.text_input("Enter your question here...")

#     with st.sidebar:
#          st.header('Your Documents')
#          st.file_uploader("Upload your documnets here...", accept_multiple_files=True)
#          st.button("Process")


# if __name__ == "__main__":
#      main()



import streamlit as st
from dotenv import load_dotenv

from src.pdf_processor import extract_pdf
from src.text_splitter import split_documents
from src.vector_store import create_vector_store
from src.rag_chain import ask_question

load_dotenv()

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="Document Assistant",
    page_icon="📚",
    layout="wide"
)

# ---------------- SESSION STATE ----------------

if "vector_store" not in st.session_state:
    st.session_state.vector_store = None

if "messages" not in st.session_state:
    st.session_state.messages = []

if "processed_files" not in st.session_state:
    st.session_state.processed_files = []

# ---------------- HEADER ----------------

st.title("📚 Document Assistant")
st.write(
    "Upload PDF documents and ask questions using "
    "Retrieval-Augmented Generation (RAG)."
)

st.divider()

# ---------------- SIDEBAR ----------------

with st.sidebar:

    st.header("📂 Upload Documents")

    uploaded_files = st.file_uploader(
        "Choose PDF files",
        type=["pdf"],
        accept_multiple_files=True
    )

    process_button = st.button(
        "Process Documents",
        type="primary",
        use_container_width=True
    )

    if process_button:

        if not uploaded_files:
            st.warning("Please upload at least one PDF.")

        else:
            try:
                all_documents = []
                valid_files = []

                progress = st.progress(0)

                for index, uploaded_file in enumerate(
                    uploaded_files
                ):

                    documents = extract_pdf(uploaded_file)

                    all_documents.extend(documents)
                    valid_files.append(uploaded_file.name)

                    progress.progress(
                        (index + 1) / len(uploaded_files)
                    )

                # Split documents
                with st.spinner("Splitting documents..."):
                    chunks = split_documents(all_documents)

                # Create embeddings and vector database
                with st.spinner("Generating embeddings..."):
                    vector_store = create_vector_store(chunks)

                # Replace previous index
                st.session_state.vector_store = vector_store
                st.session_state.messages = []
                st.session_state.processed_files = valid_files

                st.success(
                    f"Successfully processed "
                    f"{len(valid_files)} PDF files!"
                )

                st.info(f"Total chunks created: {len(chunks)}")

            except Exception as e:
                st.error(f"Document processing failed: {str(e)}")

    st.divider()

    st.subheader("Processed Documents")

    if st.session_state.processed_files:

        for filename in st.session_state.processed_files:
            st.write(f"📄 {filename}")

    else:
        st.caption("No documents processed yet.")

    if st.button("Clear Documents", use_container_width=True):

        st.session_state.vector_store = None
        st.session_state.messages = []
        st.session_state.processed_files = []

        st.rerun()

    if st.button("Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()


# ---------------- CHAT HISTORY ----------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

        if message.get("sources"):

            with st.expander("View Sources"):

                for source in message["sources"]:

                    st.write(
                        f"📄 {source['source']} | "
                        f"Page: {source['page']} | "
                        f"Chunk: {source['chunk']}"
                    )


# ---------------- QUESTION INPUT ----------------

question = st.chat_input(
    "Ask something about your documents..."
)

if question:

    if st.session_state.vector_store is None:

        st.warning(
            "Please upload and process PDF documents first."
        )

    else:

        # Display user question
        st.session_state.messages.append({
            "role": "user",
            "content": question
        })

        with st.chat_message("user"):
            st.markdown(question)

        # Generate response
        with st.chat_message("assistant"):

            with st.spinner("Searching documents..."):

                try:
                    answer, sources = ask_question(
                        st.session_state.vector_store,
                        question
                    )

                    st.markdown(answer)

                    if sources:

                        with st.expander("View Sources"):

                            for source in sources:

                                st.write(
                                    f"📄 {source['source']} | "
                                    f"Page: {source['page']} | "
                                    f"Chunk: {source['chunk']}"
                                )

                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": answer,
                        "sources": sources
                    })

                except Exception as e:

                    error_message = f"Error generating answer: {str(e)}"

                    st.error(error_message)

                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": error_message,
                        "sources": []
                    })
