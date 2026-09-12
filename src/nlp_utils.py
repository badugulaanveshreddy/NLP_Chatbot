import nltk
import string

from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer


# Download required NLTK resources
nltk.download("punkt")
nltk.download("punkt_tab")


# Create stemmer
stemmer = PorterStemmer()


def preprocess_text(text):
    """
    Preprocess text using basic NLP techniques.

    Steps:
    1. Convert text to lowercase
    2. Tokenize the sentence
    3. Remove punctuation
    4. Apply stemming
    """

    # Convert text to lowercase
    text = text.lower()

    # Tokenize the text
    tokens = word_tokenize(text)

    # Remove punctuation
    tokens = [
        token
        for token in tokens
        if token not in string.punctuation
    ]

    # Apply stemming
    stemmed_tokens = [
        stemmer.stem(token)
        for token in tokens
    ]

    return stemmed_tokens