import sqlite3

def view_data():
    conn = sqlite3.connect('events.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM events')
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    conn.close()

if __name__ == '__main__':
    view_data()
