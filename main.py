from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)
app.secret_key = 'ders-ucun-sadece-secret-key'

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sqlinjection', methods=['GET', 'POST'])
def sql_injection():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = get_db_connection()
        cursor = conn.cursor()

        # SQL INJECTION ZƏİFLİYİ (Təqdimat üçün qəsdən saxlanılıb)
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        
        try:
            cursor.execute(query)
            result = cursor.fetchone()
        except sqlite3.OperationalError as e:
            error = f"SQL Error: {e}"
            result = None

        conn.close()

        if result:
            session['username'] = result['username']
            session['role'] = result['role']
            return redirect(url_for('admin_panel'))
        elif not error:
            error = "The username or password is invalid."

    return render_template('sql_injection.html', error=error)

@app.route('/admin-panel')
def admin_panel():
    if 'username' not in session:
        return redirect(url_for('sql_injection'))
        
    conn = get_db_connection()
    
    # Əgər istifadəçi admindirsə bütün istifadəçiləri çək, user-dirsə boş siyahı göndər və ya gizlət
    if session.get('role') == 'admin':
        all_users = conn.execute("SELECT * FROM users").fetchall()
    else:
        all_users = []  # Normal user-lər üçün bazadakı istifadəçi siyahısı boş qaytarılır
        
    conn.close()
    
    return render_template('admin.html', username=session['username'], users=all_users)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        role = 'user'  # Yeni qeydiyyatdan keçənlər avtomatik 'user' olur
        
        conn = get_db_connection()
        conn.execute(
            "INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
            (username, password, role)
        )
        conn.commit()
        conn.close()
        
        return redirect(url_for('sql_injection'))
        
    return render_template('create-account.html')

if __name__ == '__main__':
    app.run(debug=True)