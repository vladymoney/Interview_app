import sqlite3

def init_db():
    conn = sqlite3.connect('app.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS data (
                        id INTEGER PRIMARY KEY,
                        type TEXT,
                        x INTEGER,
                        y INTEGER,
                        image_path TEXT,
                        message TEXT)''')
    conn.commit()
    conn.close()

def insert_data(data_type, x=None, y=None, image_path=None, message=None):
    conn = sqlite3.connect('app.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO data (type, x, y, image_path, message) VALUES (?, ?, ?, ?, ?)',
                   (data_type, x, y, image_path, message))
    conn.commit()
    conn.close()

def fetch_all_data():
    conn = sqlite3.connect('app.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM data')
    rows = cursor.fetchall()
    conn.close()
    return rows

init_db()
