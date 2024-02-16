# Text Summarization Flask Application

This project is a web-based text summarization tool that allows users to input text and receive a concise summary. It uses Flask for the backend, NLTK for processing the text, and basic HTML, CSS, and JavaScript for the front end.

## Features

- Text summarization using NLTK's tokenization and cosine similarity for sentence ranking.
- Interactive web interface for inputting text and displaying the summary.
- Customizable summary length.

## Getting Started

### Prerequisites

- Python 3.x
- Flask
- NLTK
- Pandas
- NetworkX
- Sklearn

### Installation

1. Clone the repository to your local machine:
2. Navigate to the cloned repository:
3. Install the required Python packages:
4. Run the Flask application:
5. The application will be accessible at `http://127.0.0.1:5000/` in your web browser.

## Usage

1. Open the web application in your browser.
2. Input the text you wish to summarize in the provided text area.
3. (Optional) Select the number of sentences you wish the summary to contain.
4. Click the "Summarize" button to generate and display the summary below the input area.

## How It Works

The application tokenizes the input text into sentences and words, removes stopwords, and then uses the frequency of words in each sentence to compute sentence vectors. Cosine similarity is used to measure the similarity between sentences, and the NetworkX library applies the PageRank algorithm to rank sentences based on similarity. The top-ranked sentences are then selected to form the summary.

## Frontend

The frontend is built with HTML, CSS, and JavaScript, providing a simple and intuitive user interface for inputting text and displaying the generated summary.

## Backend

The Flask application handles requests, processes text using NLTK and other libraries, and returns the summarized text to the frontend.

## Author
Rohit Negi

## Acknowledgments

- NLTK Team for the comprehensive natural language processing library.
- The Flask Team for the micro web framework.
- All contributors and users of this project.
