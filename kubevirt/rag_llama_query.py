import json
import requests
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# =========================
# 🔹 RAG: Initialization
# =========================

# 載入向量索引與文件
index = faiss.read_index("docs.index")
docs = open("docs.meta").read().splitlines()

embedder = SentenceTransformer("all-MiniLM-L6-v2")

# =========================
# 🔹 RAG: Retrieval
# =========================
def retrieve_context(question, k=2):
    """
    ✅ 這整個 function 就是 RAG 的 Retrieval
    """
    q_emb = embedder.encode([question])
    _, idx = index.search(np.array(q_emb).astype("float32"), k)
    return "\n".join(docs[i] for i in idx[0])

# =========================
# 🔹 Generation (Ollama)
# =========================
def stream_generate(prompt):
    url = "http://10.42.0.33:11434/api/generate"
    payload = {
        "model": "tinyllama",
        "prompt": prompt,
        "num_predict": 64,
        "stream": True
    }

    with requests.post(url, json=payload, stream=True) as r:
        for line in r.iter_lines():
            if line:
                data = json.loads(line)
                if "response" in data:
                    print(data["response"], end="", flush=True)
                if data.get("done"):
                    print("\n\n--- done ---")

# =========================
# 🚀 RAG Pipeline Entry
# =========================
question = "Why use virtual machines for LLM workloads?"

# ✅ RAG Step 1：檢索
context = retrieve_context(question)

# ✅ RAG Step 2：Augmented Prompt
augmented_prompt = f"""
Use the following context to answer the question.

Context:
{context}

Question:
{question}

Answer:
"""

# ✅ RAG Step 3：Generation
stream_generate(augmented_prompt)

