import sqlite3

DATABASE = 'database.db'

def setup_database():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            role TEXT NOT NULL DEFAULT 'user'
        )
    ''')

    # username üzrə axtarışları sürətləndirmək üçün indeks
    cursor.execute('''
        CREATE INDEX IF NOT EXISTS idx_users_username ON users(username)
    ''')

    cursor.execute('''
        INSERT OR IGNORE INTO users (id, username, password, role) VALUES (1, 'admin', 'admin', 'admin')
    ''')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    setup_database()