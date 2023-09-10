import streamlit as st
from generate_funcs import load_llm, generate_answer
from prompts import rag_question

#import faiss_vectorstore

def main():
    st.set_page_config(page_title="SEC Chat")
    
    st.title("SEC Litigation Chatbot")
    
    st.write("This is a prototype of a chatbot that can answer questions about SEC litigation.")
    
    # Text input
    #user_input = st.text_input("Ask a question about SEC complaints")
    #st.write(f"You typed: {user_input}")

    # Store LLM generated responses
    if "messages" not in st.session_state.keys():
        st.session_state.messages = [{"role": "assistant", "content": "What can I answer about SEC litigation?"}]

    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])
    
    # User-provided prompt
    if prompt := st.chat_input():
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)

    # Load LLM
    llm = load_llm()

    # Generate a new response if last message is not from assistant
    if st.session_state.messages[-1]["role"] != "assistant":
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = generate_answer(llm, faiss_vectorstore, rag_question, ) 
                st.write(response) 
        message = {"role": "assistant", "content": response}
        st.session_state.messages.append(message)

    # Load LLM
    llm = load_llm()
    answer = generate_answer(llm, faiss_vectorstore, input_prompt, rag_question)

if __name__ == "__main__":
    main()