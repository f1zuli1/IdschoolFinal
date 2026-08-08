import sqlite3

DATABASE = 'database.db'


def get_connection():
    return sqlite3.connect(DATABASE)


def init_schema():
    """
    Yalnız cədvəlləri yaradır. Idempotent-dir (istənilən qədər
    çağırıla bilər, data-ya heç vaxt təsir etmir). App hər başlayanda
    bunu çağırmaq təhlükəsizdir.
    """
    conn = get_connection()
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

    # Stored XSS labı üçün reviews cədvəli
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS reviews (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            author TEXT,
            text TEXT
        )
    ''')

    conn.commit()
    conn.close()


def seed_admin():
    """
    Admin istifadəçisini yaradır. Bu, avtomatik app axınının bir hissəsi
    DEYİL — yalnız `python logic.py` ilə əl ilə çağırılır. Ona görə
    admin-i database-dən silsən, app reload olanda geri gəlmir.
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT OR IGNORE INTO users (id, username, password, role)
        VALUES (1, 'admin', 'admin', 'admin')
    ''')
    conn.commit()
    conn.close()
    print("Admin istifadəçisi hazır (username: admin, password: admin)")


if __name__ == '__main__':
    init_schema()
    seed_admin()