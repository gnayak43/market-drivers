import tensorflow as tf
import nltk
import spacy

# Download the 'punkt' dataset for tokenization
nltk.download('punkt')

# TensorFlow: Simple Tensor operation
a = tf.constant(5)
b = tf.constant(3)
c = a + b

print(f"TensorFlow result: {c.numpy()}")

# NLTK: Tokenize a sample sentence
sentence = "Hello, how are you doing today?"
tokens = nltk.word_tokenize(sentence)
print(f"NLTK tokens: {tokens}")

# SpaCy: Load the small English model and process a sentence
nlp = spacy.load('en_core_web_sm')
doc = nlp("This is a simple SpaCy example.")
print(f"SpaCy tokens: {[token.text for token in doc]}")
