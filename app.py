import sqlite3
from flask import Flask, render_template, request, redirect

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/', methods=['GET', 'POST'])
def login():
    error = ""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db_connection()
        try:
            db.execute(
                f"SELECT * FROM users WHERE username = {username} AND password = {password}")
            print(
                f"SELECT * FROM users WHERE username = {username} AND password = {password}")
        except sqlite3.OperationalError:
            print('erreur épargnée mdr')
            db.close()
            error = "Mauvais identifiants"
            return render_template('login.html', error=error)
        db.close()
        print("bon identifiants")
    return redirect("/home", username=username)


@app.route('/home')
def home():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
