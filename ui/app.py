import streamlit as st
from generate_funcs import load_llm, generate_answer
from prompts import rag_question

#import faiss_vectorstore

def main():
    st.title("SEC Complaint Chatbot")
    
    st.write("This is a prototype of a chatbot that can answer questions about SEC complaints.")
    
    # Text input
    user_input = st.text_input("Ask a question about SEC complaints")
    st.write(f"You typed: {user_input}")

    # Load LLM
    llm = load_llm()
    answer = generate_answer(llm, faiss_vectorstore, input_prompt, rag_question)

if __name__ == "__main__":
    main()