from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

# ---------------- MySQL Configuration ----------------
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'admin'
app.config['MYSQL_DB'] = 'lucky'

mysql = MySQL(app)

# ---------------- Routes ----------------

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/info')
def info():
    return render_template('info.html')

@app.route('/lyric')
def lyric():
    return render_template('lyric.html')

@app.route('/display')
def display():
    song = "Example song lyric"
    return render_template('display.html', song=song)

# 🧾 GET Method Form Submission Route
@app.route('/submit', methods=['GET'])
def submit():
    username = request.args.get('username')
    password = request.args.get('password')

    if username and password:
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO students(name, password) VALUES (%s, %s)", (username, password))
        mysql.connection.commit()
        cur.close()
        return 'Form Submitted Successfully!'
    else:
        return 'Please enter both username and password.'

# ---------------- Main ----------------
if __name__ == '__main__':
    app.run(debug=True)
