from langchain.llms import HuggingFacePipeline
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

from config import llm_model_name
#from prompts import rag_question

def load_llm():
    
    """Loads the LLM model."""
    
    llm = HuggingFacePipeline.from_model_id(
    model_id=llm_model_name,
    task="text-generation",
    pipeline_kwargs={"max_new_tokens": 10},)
    
    return llm


def generate_answer(llm,faiss_vectorstore,input_prompt,query):
    
    """Generates answers from a query."""

    # Define QA chain
    qa_chain = RetrievalQA.from_chain_type(
    llm,
    retriever=faiss_vectorstore.as_retriever(),
    chain_type_kwargs={"prompt": input_prompt})

    result = qa_chain({"query": query})
    
    return result["result"]




