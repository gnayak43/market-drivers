import nltk
import spacy

nltk.download('punkt')
nlp = spacy.load('en_core_web_sm')

def preprocess_article(article_text):
    sentences = nltk.sent_tokenize(article_text)
    processed_sentences = []
    for sentence in sentences:
        doc = nlp(sentence)
        processed_sentence = ' '.join([token.lemma_ for token in doc if not token.is_stop])
        processed_sentences.append(processed_sentence)
    return ' '.join(processed_sentences)

# Example usage
if __name__ == "__main__":
    example_text = "The EUR/USD is experiencing a rise due to market conditions."
    print(preprocess_article(example_text))
