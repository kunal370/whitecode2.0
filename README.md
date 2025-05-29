# ⛑️ whitecode2.0 - Hybrid AI Code Assistant 🤖💻

**whitecode2.0** is a smart Python coding assistant powered by **ChromaDB**, **Sentence Transformers**, and **Gemini**. It provides contextual code suggestions and explanations for Python questions using both locally trained code snippets and generative AI when necessary.

---

## 🚀 Features

- 🔎 Searches a local ChromaDB for matching Python code examples.
- 🤖 Falls back to Gemini API when no local match is found.
- 💬 Chat-style interface built with **Streamlit**.
- 🧠 Uses `all-MiniLM-L6-v2` from SentenceTransformers to embed and query code.
- 🗂️ Locally stores and retrieves Python files from a `data/` folder.
- 📚 Pre-trained code snippets (80+ examples)
- ☁️ Gemini API for complex queries
---


## ✅ Example Questions
Try asking:

WAF to convert USD to INR.

Write a recursive function to calculate the sum of first n natural numbers.

Print 100 to 50 odd numbers in reverse order

Hi


    
- ✨ **Beautifully Formatted Responses**: Code blocks with proper indentation and syntax highlighting
- 🌐 **Web Interface**: Simple and intuitive chat-like interface
- 🔒 **Secure**: API keys protected via environment variables


- **Smart Response Handling**:
  ```python
  if question in local_knowledge:
      return trained_response
  else:
      return gemini_response

Ask coding questions, hit send, and whitecode 2.0 responds instantly!
## Demo
![image](https://github.com/user-attachments/assets/7d9d94f0-1907-4ec9-ad41-d824756b7e15)
![image](https://github.com/user-attachments/assets/1a939f3f-2f1e-48df-8c8e-85e0f35afd05)
![image](https://github.com/user-attachments/assets/c59a08de-b3e6-4a32-b7cf-bd59b1f8c715)




