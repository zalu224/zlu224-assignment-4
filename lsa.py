import numpy as np
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
from sklearn.metrics.pairwise import cosine_similarity

class LatentSemanticAnalyzer:
    def __init__(self):
        # Load the dataset
        newsgroups = fetch_20newsgroups(subset='all')
        self.documents = newsgroups.data
        
        # Create a TF-IDF matrix
        self.vectorizer = TfidfVectorizer(stop_words='english', max_features=1000)
        self.term_doc_matrix = self.vectorizer.fit_transform(self.documents)
        
        # Apply SVD (LSA)
        self.svd_model = TruncatedSVD(n_components=100)
        self.lsa_matrix = self.svd_model.fit_transform(self.term_doc_matrix)

    def search(self, query):
        # Vectorize the query
        query_vec = self.vectorizer.transform([query])
        query_lsa = self.svd_model.transform(query_vec)
        
        # Calculate cosine similarity between the query and all documents
        similarities = cosine_similarity(query_lsa, self.lsa_matrix)[0]
        
        # Get top 5 most similar documents
        top_indices = np.argsort(similarities)[::-1][:5]
        top_similarities = similarities[top_indices]
        top_documents = [self.documents[i] for i in top_indices]
        
        return top_documents, top_similarities
