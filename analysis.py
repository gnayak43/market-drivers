from textblob import TextBlob
import spacy

nlp = spacy.load('en_core_web_sm')

def analyze_article(processed_text):
    sentiment = TextBlob(processed_text).sentiment.polarity
    surge_keywords = ['increase', 'rise', 'growth', 'bullish']
    drop_keywords = ['decrease', 'fall', 'decline', 'bearish']
    
    surge_count = sum([processed_text.count(word) for word in surge_keywords])
    drop_count = sum([processed_text.count(word) for word in drop_keywords])

    if sentiment > 0.1 and surge_count > drop_count:
        return 'Trade Volume Up'
    elif sentiment < -0.1 and drop_count > surge_count:
        return 'Trade Volume Down'
    else:
        return 'No Significant Movement'

def extract_currency_pairs(article_text):
    currency_pairs = []
    doc = nlp(article_text)
    for ent in doc.ents:
        if ent.label_ == "MONEY":
            currency_pairs.append(ent.text)
    return currency_pairs

# Example usage
if __name__ == "__main__":
    processed_text = "The market is bullish, and the USD is expected to rise."
    result = analyze_article(processed_text)
    print(result)

    currency_pairs = extract_currency_pairs(processed_text)
    print(f"Currency Pairs: {currency_pairs}")
