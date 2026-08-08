from flask import Flask, render_template, request, redirect, url_for, session, make_response
from markupsafe import Markup
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

        # SQL INJECTION VULNERABILITY (kept intentionally for demo)
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

            resp = make_response(redirect(url_for('admin_panel')))
            resp.set_cookie('session_token', f"demo-token-{result['username']}", httponly=False)
            return resp
        elif not error:
            error = "The username or password is invalid."

    return render_template('sql_injection.html', error=error)

@app.route('/admin-panel')
def admin_panel():
    if 'username' not in session:
        return redirect(url_for('sql_injection'))

    conn = get_db_connection()

    if session.get('role') == 'admin':
        all_users = conn.execute("SELECT * FROM users").fetchall()
    else:
        all_users = []

    conn.close()

    return render_template('admin.html', username=session['username'], users=all_users)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        role = 'user'

        conn = get_db_connection()
        conn.execute(
            "INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
            (username, password, role)
        )
        conn.commit()
        conn.close()

        return redirect(url_for('sql_injection'))

    return render_template('create-account.html')

# ----------------------------------------------------------------------
# XSS lab index
# ----------------------------------------------------------------------
@app.route('/xss')
def xss_overview():
    resp = make_response(render_template('xss.html'))
    resp.set_cookie('session_token', 'demo-token-12345', httponly=False)
    return resp

# ----------------------------------------------------------------------
# Lab: product page with reviews
# ----------------------------------------------------------------------
@app.route('/xss/stored', methods=['GET', 'POST'])
def xss_stored():
    conn = get_db_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS reviews (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            author TEXT,
            text TEXT
        )
    """)

    if request.method == 'POST':
        author = request.form.get('author', 'Anonymous')
        comment = request.form['comment']
        conn.execute("INSERT INTO reviews (author, text) VALUES (?, ?)", (author, comment))
        conn.commit()

    rows = conn.execute("SELECT author, text FROM reviews ORDER BY id DESC").fetchall()
    conn.close()

    comments = [{'author': Markup(row['author']), 'text': Markup(row['text'])} for row in rows]

    resp = make_response(render_template('xss_stored.html', comments=comments))
    resp.set_cookie('coockie', 'asdf1234', httponly=False)
    return resp

# ----------------------------------------------------------------------
# Lab: search page
# ----------------------------------------------------------------------
@app.route('/xss/reflected')
def xss_reflected():
    query = request.args.get('q', '')
    safe_or_not = Markup(query) if query else ''

    resp = make_response(render_template('xss_reflected.html', query=safe_or_not, raw_query=query))
    resp.set_cookie('coockie', 'asdfasdf1234', httponly=False)
    return resp

# ----------------------------------------------------------------------
# Lab: client-side greeting widget
# ----------------------------------------------------------------------
@app.route('/xss/dom')
def xss_dom():
    resp = make_response(render_template('xss_dom.html'))
    resp.set_cookie('coockie', 'asdfasdfasdf1234', httponly=False)
    return resp

if __name__ == '__main__':
    app.run(debug=True)