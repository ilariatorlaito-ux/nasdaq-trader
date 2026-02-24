from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

NEWS_API_KEY = os.environ.get("NEWS_API_KEY")

@app.route("/")
def home():
    return "Server NASDAQ Trader attivo"

@app.route("/news")
def news():
    url = f"https://newsapi.org/v2/everything?q=nasdaq&language=en&sortBy=publishedAt&apiKey={NEWS_API_KEY}"
    r = requests.get(url)
    data = r.json()

    articles = []
    for a in data.get("articles", [])[:5]:
        articles.append({
            "title": a["title"],
            "url": a["url"],
            "source": a["source"]["name"]
        })

    return jsonify(articles)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
