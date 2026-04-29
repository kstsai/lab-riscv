
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# 1️⃣ 載入文件
docs = [line.strip() for line in open("docs.txt") if line.strip()]

# 2️⃣ Embedding model（輕量、快）
embedder = SentenceTransformer("all-MiniLM-L6-v2")

# 3️⃣ 將文件轉成向量 ✅（Embedding）
embeddings = embedder.encode(docs)

# 4️⃣ 建立 FAISS index ✅（Vector DB）
dim = embeddings.shape[1]
index = faiss.IndexFlatL2(dim)
index.add(np.array(embeddings).astype("float32"))

# 5️⃣ 存檔
faiss.write_index(index, "docs.index")
with open("docs.meta", "w") as f:
    f.write("\n".join(docs))

print("✅ Vector index built")

