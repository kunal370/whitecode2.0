import streamlit as st
import google.generativeai as genai
import chromadb
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv
import os
import re

# Load environment variables
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
gemini = genai.GenerativeModel('gemini-2.0-flash')

# Setup ChromaDB
chroma = chromadb.PersistentClient(path="models/db").get_collection("code_snippets")
embedder = SentenceTransformer('all-MiniLM-L6-v2')

# Streamlit app config
st.set_page_config(page_title="whitecode2.0", page_icon="⛑️")
st.title("whitecode2.0 - Python Coding Assistant")


def format_code_block(code):
    """Ensure perfect indentation and formatting for code blocks"""
    lines = code.split('\n')
    while lines and not lines[0].strip():
        lines.pop(0)
    while lines and not lines[-1].strip():
        lines.pop()

    min_indent = min(len(line) - len(line.lstrip()) for line in lines if line.strip())
    formatted_lines = [line[min_indent:] if line.strip() else '' for line in lines]
    return '\n'.join(formatted_lines)


def get_response(question):
    """Handle question processing and response generation"""
    # Handle greetings
    if question.lower() in ['hi', 'hello', 'hey']:
        return {
            "answer": "Hello! I'm whitecode2.0. Ask me Python coding questions.",
            "is_code": False,
            "source": "system"
        }

    # Try local ChromaDB first for code questions
    if any(keyword in question.lower() for keyword in
           ['to', 'wap', 'WAF', 'code', 'example', 'write', 'create', 'implement', 'how', 'WAP']):
        results = chroma.query(
            query_embeddings=embedder.encode([question]).tolist(),
            n_results=1
        )

        if results["documents"]:
            code = format_code_block(results["documents"][0][0])
            return {
                "answer": code,
                "is_code": True,
                "source": "trained data"
            }

    # Fallback to Gemini
    prompt = f"""Provide a response to this Python question with perfect indentation:
    Question: {question}

    Requirements:
    1. If answering with code, use exactly 4 spaces for indentation
    2. Wrap code in markdown code blocks
    3. Keep explanations concise"""

    response = gemini.generate_content(prompt)
    return {
        "answer": response.text,
        "is_code": "```python" in response.text,
        "source": "gemini"
    }


# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        if message["is_code"]:
            st.code(message["content"], language='python')
        else:
            st.markdown(message["content"])

        if message["source"] != "system":
            st.caption(f"Source: {message['source']}")

# Accept user input
if prompt := st.chat_input("Ask a Python question..."):
    # Add user message to chat history
    st.session_state.messages.append({
        "role": "user",
        "content": prompt,
        "is_code": False,
        "source": "user"
    })

    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get and display response
    with st.spinner("Thinking..."):
        response = get_response(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        if response["is_code"]:
            st.code(response["answer"], language='python')
        else:
            st.markdown(response["answer"])

        if response["source"] != "system":
            st.caption(f"Source: {response['source']}")

    # Add assistant response to chat history
    st.session_state.messages.append({
        "role": "assistant",
        "content": response["answer"],
        "is_code": response["is_code"],
        "source": response["source"]
    })