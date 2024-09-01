from fetch_articles import fetch_articles
from text_processing import preprocess_article
from analysis import analyze_article, extract_currency_pairs

# Fetch articles from Bloomberg and Reuters
bloomberg_url = 'https://www.bloomberg.com/markets'
reuters_url = 'https://www.reuters.com/finance'
bloomberg_articles = fetch_articles(bloomberg_url)
reuters_articles = fetch_articles(reuters_url)
articles = bloomberg_articles + reuters_articles

# Process and analyze each article
for article_text, url in articles:
    processed_text = preprocess_article(article_text)
    analysis_result = analyze_article(processed_text)
    currency_pairs = extract_currency_pairs(article_text)
    
    print(f"Result: {analysis_result} | URL: {url} | Currency Pairs: {', '.join(currency_pairs) if currency_pairs else 'N/A'}")
