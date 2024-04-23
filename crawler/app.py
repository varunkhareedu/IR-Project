from flask import Flask, request, render_template, jsonify
import pickle
import numpy as np
from nltk.corpus import wordnet as wn

app = Flask(__name__)

# Load the inverted index for search operations
with open('index.pkl', 'rb') as f:
    inverted_index = pickle.load(f)


def expand_query(query):
    expanded_terms = set()
    for word in query.split():
        synsets = wn.synsets(word)
        for syn in synsets:
            for lemma in syn.lemmas():
                expanded_terms.add(lemma.name().replace('_', ' '))
    return ' '.join(expanded_terms)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        query = request.form.get('query')
        k = int(request.form.get('k', 5))
        if not query:
            return render_template('index.html', error="Please enter a search query")

        valid, message = validate_query(query)
        if not valid:
            return render_template('index.html', error=message)

        expanded_query = expand_query(query)
        result_indices = rank_documents(query, k)

        response = {
            'original_query': query,
            'expanded_query': expanded_query,
            'results': [f'Document {i}' for i in result_indices]
        }
        return render_template('results.html', response=response)

    return render_template('index.html')


def validate_query(query):
    if not query:
        return False, "Query cannot be empty."
    return True, ""


def rank_documents(query, k):
    query_terms = query.lower().split()
    doc_scores = {doc_id: 0 for doc_id in range(len(inverted_index))}
    for term in query_terms:
        if term in inverted_index:
            for doc_id, weight in inverted_index[term].items():
                doc_scores[doc_id] += weight
    sorted_docs = sorted(doc_scores.items(),
                         key=lambda item: item[1], reverse=True)
    return [doc[0] for doc in sorted_docs[:k]]


if __name__ == '__main__':
    app.run(debug=True)
