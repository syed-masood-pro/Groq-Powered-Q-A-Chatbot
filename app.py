import streamlit as st # type: ignore
from langchain_groq import ChatGroq # type: ignore
from langchain_core.output_parsers import StrOutputParser # type: ignore
from langchain_core.prompts import ChatPromptTemplate # type: ignore
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "Simple Q&A Chatbot with Grok"

# Define prompt properly
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the user queries"),
        ("user", "Question: {question}")
    ]
)

def generate_response(question, api_key, llm, temperature, max_tokens):
    llm = ChatGroq(
        groq_api_key=api_key,
        model_name=llm,
        temperature=temperature,
        max_tokens=max_tokens
    )
    chain = prompt | llm | StrOutputParser()
    response = chain.invoke({"question": question})
    return response

st.title("Enhanced Q&A Chatbot with Groq")

st.sidebar.title("Settings")
api_key = st.sidebar.text_input("Enter your GROQ AI API Key: ", type="password")

llm = st.sidebar.selectbox(
    "Select a LLM Model",
    ["llama-3.3-70b-versatile", "openai/gpt-oss-20b", "gemma2-9b-it", "deepseek-r1-distill-llama-70b"]
)

temperature = st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, value=0.7)
max_tokens = st.sidebar.slider("Max Tokens", min_value=50, max_value=300, value=150)

st.write("Go ahead and ask any question")

user_input = st.text_input("You: ")

if user_input and api_key:
    response = generate_response(user_input, api_key, llm, temperature, max_tokens)
    st.write("AI: ", response)
elif not api_key:
    st.warning("Please enter your GROQ API Key in the sidebar.")

