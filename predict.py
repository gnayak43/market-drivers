# Make Predictions: After the model is trained, use the predict.py script to predict new articles - python predict.py
import joblib
from process_articles import preprocess_article

# Load the trained model
model = joblib.load('fx_trade_volume_model.pkl')

def predict_article(article):
    processed_article = preprocess_article(article)
    prediction = model.predict([processed_article])
    return prediction[0]

if __name__ == "__main__":
    # Example: Predicting a new article (replace with actual content)
    new_article = """The EUR/USD pair is expected to surge due to positive economic data."""
    prediction = predict_article(new_article)
    print(f"Predicted trade volume change: {prediction}")
