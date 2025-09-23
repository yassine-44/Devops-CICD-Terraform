from flask import Flask, render_template
import requests
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(message)s'
)
logger = logging.getLogger(__name__)

app = Flask(__name__)
WIKI_RANDOM_URL = "https://en.wikipedia.org/api/rest_v1/page/random/summary"

@app.route('/')
def index():
    headers = {"User-Agent": "MyWikiReader/1.0 (https://github.com/yassinekrout)"}
    try:
        response = requests.get(WIKI_RANDOM_URL, headers=headers, timeout=10)
        if response.status_code == 200:
            data = response.json()
            article = {
                "title": data["title"],
                "extract": data["extract"],
                "url": data["content_urls"]["desktop"]["page"]
            }
        else:
            article = {"title": f"HTTP {response.status_code}", "extract": "Failed to load."}
    except Exception as e:
        logger.error("Request failed: %s", e)
        article = {"title": "Request Failed", "extract": "Check network."}
    
    return render_template('index.html', article=article)

if __name__ == '__main__':
    logger.info("App started on port 5000")
    app.run(host='0.0.0.0', port=5000)