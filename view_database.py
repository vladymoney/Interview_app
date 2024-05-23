import sqlite3

def view_data():
    conn = sqlite3.connect('app.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM data')
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    conn.close()

if __name__ == '__main__':
    view_data()
