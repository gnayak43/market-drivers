import os
import nltk
from sklearn.model_selection import train_test_split

nltk.download('punkt')

def load_articles(directory):
    articles = []
    labels = []
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            with open(os.path.join(directory, filename), 'r') as file:
                content = file.read()
                articles.append(content)
                # Assuming you have labels in filenames (e.g., article_surge.txt)
                if 'surge' in filename:
                    labels.append('up')
                elif 'drop' in filename:
                    labels.append('down')
                else:
                    labels.append('no_change')
    return articles, labels

def preprocess_article(article):
    sentences = nltk.sent_tokenize(article)
    words = [nltk.word_tokenize(sentence) for sentence in sentences]
    flattened_words = [word for sublist in words for word in sublist]
    return ' '.join(flattened_words)

if __name__ == "__main__":
    articles, labels = load_articles('articles')
    processed_articles = [preprocess_article(article) for article in articles]
    
    # Example of splitting data for training and testing
    X_train, X_test, y_train, y_test = train_test_split(processed_articles, labels, test_size=0.2, random_state=42)
    print(f"Training on {len(X_train)} articles, testing on {len(X_test)} articles")
