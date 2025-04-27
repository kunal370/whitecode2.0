from flask import Flask, request, jsonify, render_template
import google.generativeai as genai
import chromadb
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv
import os
import re

load_dotenv()

app = Flask(__name__)
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
gemini = genai.GenerativeModel('gemini-2.0-flash')

# Setup ChromaDB
chroma = chromadb.PersistentClient(path="models/db").get_collection("code_snippets")
embedder = SentenceTransformer('all-MiniLM-L6-v2')


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


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/ask", methods=["POST"])
def ask():
    question = request.form["question"].strip()

    # Handle greetings
    if question.lower() in ['hi', 'hello', 'hey']:
        return jsonify({
            "answer": "Hello! I'm whitecode2.0. Ask me Python coding questions.",
            "is_code": False,
            "source": "system"
        })

    # Try local ChromaDB first for code questions
    if any(keyword in question.lower() for keyword in ['to','wap','WAF', 'code', 'example', 'write', 'create', 'implement','how','WAP',]):
        results = chroma.query(
            query_embeddings=embedder.encode([question]).tolist(),
            n_results=1
        )

        if results["documents"]:
            code = format_code_block(results["documents"][0][0])
            return jsonify({
                "answer": f"```python\n{code}\n```",
                "is_code": True,
                "source": "trained data"
            })

    # Fallback to Gemini
    prompt = f"""Provide a response to this Python question with perfect indentation:
    Question: {question}

    Requirements:
    1. If answering with code, use exactly 4 spaces for indentation
    2. Wrap code in markdown code blocks
    3. Keep explanations concise"""

    response = gemini.generate_content(prompt)
    return jsonify({
        "answer": response.text,
        "is_code": "```python" in response.text,
        "source": "gemini"
    })


if __name__ == "__main__":
    app.run(debug=True)