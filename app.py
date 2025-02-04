from flask import Flask, jsonify
import requests

app = Flask(__name__)

# Replace this with your actual NewsAPI key
API_KEY = "3bffaf5804fb4ef5b5974128bc1781f8"

@app.route('/')
def home():
    return "Forex News App Backend is Running!"

@app.route('/news', methods=['GET'])
def get_news():
    url = f"https://newsapi.org/v2/everything?q=forex&language=en&apiKey={API_KEY}"
    response = requests.get(url)
    data = response.json()

    # Extract only the top 5 news articles
    articles = data.get("articles", [])[:5]
    return jsonify(articles)

if __name__ == '__main__':
    app.run(debug=True)
    
git add requirements.txt
git status
git commit -m "Added requirements.txt for Render deployment"
git push origin main
