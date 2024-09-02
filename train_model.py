# Train the Model, Run the train_model.py script to train the logistic regression model - python train_model.py

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
from process_articles import load_articles, preprocess_article

# Load and preprocess articles
articles, labels = load_articles('articles')
processed_articles = [preprocess_article(article) for article in articles]

# Split data into training and test sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(processed_articles, labels, test_size=0.2, random_state=42)

# Create a pipeline that includes TF-IDF vectorization and logistic regression
pipeline = Pipeline([
    ('vectorizer', TfidfVectorizer()),  # Converts text into a matrix of TF-IDF features
    ('classifier', LogisticRegression())  # Logistic Regression classifier
])

# Train the model
pipeline.fit(X_train, y_train)

# Evaluate the model
y_pred = pipeline.predict(X_test)
print(classification_report(y_test, y_pred))

# Save the model for future use
import joblib
joblib.dump(pipeline, 'fx_trade_volume_model.pkl')
