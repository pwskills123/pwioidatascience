from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# Database connection
def get_db_connection():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='1nc12ec049',
        database='registration_db'
    )
    return conn

@app.route('/')
def index():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (username, email, password) VALUES (%s, %s, %s)',
                   (username, email, password))
    conn.commit()
    cursor.close()
    conn.close()

    return redirect('/')

@app.route('/users')
def users():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT id, username, email FROM users')
    users_data = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('users.html', users=users_data)


if __name__ == '__main__':
    app.run(debug=True)
