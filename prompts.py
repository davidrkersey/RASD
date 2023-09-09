rag_question = """Use the following pieces of context (delimited by <ctx></ctx>) to answer the question at the end. 
If you don't know the answer, just say that you don't know, don't try to make up an answer. 
Use three sentences maximum and keep the answer as concise as possible. 
-----
<ctx>
{context}
</ctx>
-----
Question: {question}
Helpful Answer: """