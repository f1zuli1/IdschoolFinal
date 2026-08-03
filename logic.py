import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Cədvəl yaratmaq (Role sütunu əlavə olundu)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL,
        role TEXT NOT NULL DEFAULT 'user'
    )
''')

# Admin istifadəçisini əlavə etmək
cursor.execute('''
    INSERT OR IGNORE INTO users (id, username, password, role) VALUES (1, 'admin', 'admin', 'admin')
''')

conn.commit()
conn.close()