import sqlite3

def init_db():
    try:
        conn = sqlite3.connect('app.db')
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS events (
                            id INTEGER PRIMARY KEY,
                            type TEXT,
                            x INTEGER,
                            y INTEGER,
                            image_path TEXT,
                            message TEXT)''')
        conn.commit()
        print("Database initialized successfully")
    except sqlite3.Error as e:
        print("Error initializing database:", e)

def insert_data(data_type, x=None, y=None, image_path=None, message=None):
    try:
        conn = sqlite3.connect('app.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO events (type, x, y, image_path, message) VALUES (?, ?, ?, ?, ?)',
                       (data_type, x, y, image_path, message))
        conn.commit()
        print("Data inserted successfully")
    except sqlite3.Error as e:
        print("Error inserting data:", e)

def fetch_all_data():
    try:
        conn = sqlite3.connect('app.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM events')
        rows = cursor.fetchall()
        conn.close()
        return rows
    except sqlite3.Error as e:
        print("Error fetching data:", e)
        return []

init_db()
