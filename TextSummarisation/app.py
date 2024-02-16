import os
import pandas as pd
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from sklearn.metrics.pairwise import cosine_similarity
import networkx as nx
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Load NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

# Function to summarize text
def summarize_text(text, num_sentences=3):  
    # Tokenize the sentences in the input text
    sentences = sent_tokenize(text)

    # Preprocess the sentences (lowercase, remove stopwords, punctuation)
    stop_words = set(stopwords.words('english'))
    preprocessed_sentences = [
        [word.lower() for word in word_tokenize(sentence) if word.lower() not in stop_words and word.isalnum()] for
        sentence in sentences]

    # Compute sentence vectors using frequency distribution
    sentence_vectors = [nltk.FreqDist(sentence) for sentence in preprocessed_sentences]
    max_length = max(len(sentence) for sentence in sentence_vectors)  # Find the maximum length of sentence vectors
    sentence_vectors = [list(sentence.values()) + [0] * (max_length - len(sentence)) for sentence in
                        sentence_vectors]  # Pad sentence vectors with zeros

    # Compute cosine similarity matrix
    similarity_matrix = cosine_similarity(sentence_vectors)

    # Convert the similarity matrix to a graph
    graph = nx.from_numpy_array(similarity_matrix)

    # Apply PageRank algorithm to rank sentences
    scores = nx.pagerank(graph)

    # Sort sentences based on their PageRank scores
    ranked_sentences = sorted(((scores[i], sentence) for i, sentence in enumerate(sentences)), reverse=True)

    # Select top-ranked sentences to form the summary
    num_sentences = min(len(ranked_sentences), num_sentences)  # Set the number of sentences in the summary
    summary = ' '.join(sentence for score, sentence in ranked_sentences[:num_sentences])

    return summary


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    text = request.json['text']
    num_sentences = int(request.json.get('numSentences', 3))  # Get numSentences value from request
    summary = summarize_text(text, num_sentences)  # Pass num_sentences to summarize_text function
    print(summary)
    return jsonify({'summary': summary})

if __name__ == '__main__':
    app.run(debug=True)
