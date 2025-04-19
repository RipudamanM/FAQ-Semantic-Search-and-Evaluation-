import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load model and data
model = SentenceTransformer('all-MiniLM-L6-v2')
faq_data = pd.read_csv('data.csv')
faq_embeddings = model.encode(faq_data['Question'].tolist(), convert_to_tensor=False)

def search_faq(query):
    query_embedding = model.encode([query])
    similarity_scores = cosine_similarity(query_embedding, faq_embeddings)[0]
    top_index = similarity_scores.argmax()

    return {
        "question": faq_data['Question'][top_index],
        "answer": faq_data['Answer'][top_index],
        "score": f"{similarity_scores[top_index]:.4f}"
    }
