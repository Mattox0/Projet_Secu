import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect('database.db')
    return conn.cursor()


@app.route('/', methods=['GET', 'POST'])
def login():
    error = ""
    if request.method == 'POST':
        username = request.form['login']
        password = request.form['password']
        db = get_db_connection()
        db.execute(
            f"SELECT * FROM users WHERE username=? AND password=?", [username, password])
        row = db.fetchone()
        if row == None:
            db.close()
            error = "Error Wrong credentials"
            return render_template('login.html', error=error)
        db.close()
        return render_template("index.html", username=row[1])
    return render_template('login.html')


if __name__ == "__main__":
    app.run(debug=True)
