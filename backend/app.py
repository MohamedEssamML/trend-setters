from flask import Flask, jsonify
from flask_cors import CORS
from scraper import scrape_tiktok_trends
from ai_processor import generate_content
from database import init_db, save_trend
from scheduler import start_scheduler
import sqlite3

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend

@app.route('/api/trends', methods=['GET'])
def get_trends():
    trends = scrape_tiktok_trends()
    contents = generate_content(trends)
    for trend, content in zip(trends, contents):
        save_trend(trend['hashtag'], trend['views'], content)
    conn = sqlite3.connect('trends.db')
    cursor = conn.cursor()
    cursor.execute('SELECT hashtag, views, content FROM trends')
    data = [{"hashtag": row[0], "views": row[1], "content": row[2]} for row in cursor.fetchall()]
    conn.close()
    return jsonify(data)

if __name__ == '__main__':
    init_db()
    start_scheduler()
    app.run(debug=True, port=5000)