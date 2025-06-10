import sqlite3

def init_db():
    conn = sqlite3.connect('trends.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS trends (
            id INTEGER PRIMARY KEY,
            hashtag TEXT,
            views TEXT,
            content TEXT
        )
    ''')
    conn.commit()
    conn.close()

def save_trend(hashtag, views, content):
    conn = sqlite3.connect('trends.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO trends (hashtag, views, content) VALUES (?, ?, ?)',
                   (hashtag, views, content))
    conn.commit()
    conn.close()