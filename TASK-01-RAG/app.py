import streamlit as st

def main():
    st.set_page_config(page_title="Ask about your DOCs", page_icon=":books:")
    st.header("Ask about your DOCs :books:")
    st.text_input("Enter your question here...")

    with st.sidebar:
         st.header('Your Documents')
         st.file_uploader("Upload your documnets here...")
         st.button("Process")











if __name__ == "__main__":
     main()