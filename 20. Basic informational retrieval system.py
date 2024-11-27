from sklearn.feature_extraction.text import TfidfVectorizer

# Corpus of documents
documents = [
    "The cat sat on the mat.",
    "The dog barked at the postman.",
    "The cat and the dog are friends.",
]

# TF-IDF Vectorization
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(documents)

# Display TF-IDF scores
print("TF-IDF Matrix:")
print(tfidf_matrix.toarray())
print("\nFeature Names:")
print(vectorizer.get_feature_names_out())

# Query for ranking documents
query = "cat and dog"
query_vec = vectorizer.transform([query])

# Compute similarity scores
from sklearn.metrics.pairwise import cosine_similarity
scores = cosine_similarity(query_vec, tfidf_matrix)

print("\nDocument Scores:")
for idx, score in enumerate(scores[0]):
    print(f"Document {idx + 1}: {score:.2f}")
