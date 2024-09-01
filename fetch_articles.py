import requests
from bs4 import BeautifulSoup

def fetch_articles(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    articles = soup.find_all('article')
    return [(article.text, article.find('a')['href']) for article in articles]

# Example usage
if __name__ == "__main__":
    bloomberg_url = 'https://www.bloomberg.com/markets'
    reuters_url = 'https://www.reuters.com/finance'
    bloomberg_articles = fetch_articles(bloomberg_url)
    reuters_articles = fetch_articles(reuters_url)
    articles = bloomberg_articles + reuters_articles
    print(articles)
