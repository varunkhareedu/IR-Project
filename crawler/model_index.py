import os
import pickle
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import TfidfVectorizer


def fetch_text(directory_path):
    document_texts = []
    # List all files in the given directory that end with '.html'
    for file_name in os.listdir(directory_path):
        if file_name.endswith('.html'):
            file_path = os.path.join(directory_path, file_name)
            with open(file_path, 'r', encoding='utf-8') as file:
                parsed_html = BeautifulSoup(file, 'html.parser')
                document_texts.append(parsed_html.get_text())
    return document_texts


def generate_tfidf(document_texts):
    tfidf_gen = TfidfVectorizer(stop_words='english')
    tfidf_values = tfidf_gen.fit_transform(document_texts)
    return tfidf_gen, tfidf_values


def create_inverted_index(tfidf_values, tfidf_gen):
    index = {}
    terms = tfidf_gen.get_feature_names_out()
    for idx, term in enumerate(terms):
        document_indices = tfidf_values[:, idx].nonzero()[0]
        index[term] = {i: tfidf_values[i, idx] for i in document_indices}
    return index


# Path to the directory containing HTML files
directory_path = 'downloaded_pages'

texts = fetch_text(directory_path)
tfidf_gen, tfidf_values = generate_tfidf(texts)
index = create_inverted_index(tfidf_values, tfidf_gen)

# Saving the inverted index to a pickle file
with open('index.pkl', 'wb') as index_file:
    pickle.dump(index, index_file)

print("Inverted index has been built and saved.")
