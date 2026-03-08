import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Load data
with open("cyber_laws.json", "r") as f:
    laws_data = json.load(f)

# Prepare docs for indexing
docs = []
metadata = []
for law in laws_data:
    doc = f"{law['law']} Section {law['section']}:\n{law['description']['verbatim']}\n" \
          f"Layman Explanation: {law['description']['layman_terms']}\nExample: {law['description']['example']}"
    docs.append(doc)
    metadata.append({
        "law": law["law"],
        "section": law["section"],
        "offence": law["offence"],
        "punishment": law["punishment"]
    })

# Sentence Transformer model
model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = model.encode(docs, convert_to_tensor=False)

# FAISS index
dimension = embeddings[0].shape[0]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings))

def search_law(query, top_k=3):  
    query_vector = model.encode([query])[0]
    D, I = index.search(np.array([query_vector]), top_k)

    results = []
    for score, idx in zip(D[0], I[0]):
        if score < 1.0:  
            result = {
                "match": docs[idx],
                "meta": metadata[idx],
                "score": score
            }
            results.append(result)
    return results
