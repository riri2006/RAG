from sklearn.feature_extraction.text import CountVectorizer

documents = [
    "I love Python",
    "I love Machine Learning"
]

vectorizer = CountVectorizer()
sparse_vectors = vectorizer.fit_transform(documents)

print(vectorizer.get_feature_names_out())
print(sparse_vectors.toarray())