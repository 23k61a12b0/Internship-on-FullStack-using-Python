from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL

app1 = Flask(__name__)


app1.config['MYSQL_HOST'] = 'localhost'
app1.config['MYSQL_USER'] = 'root'
app1.config['MYSQL_PASSWORD'] = 'admin'
app1.config['MYSQL_DB'] = 'lucky'

mysql = MySQL(app1)

@app1.route('/')
def form():
    return render_template('info.html')

@app1.route('/submit', methods=['GET'])
def submit():
    if request.method == 'GET':
        username = request.form['username']
        password = request.form['password']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO students(name,password) VALUES(lucky,admin)", (name , password))
        mysql.connection.commit()
        cur.close()

        return 'Form Submitted Successfully!'

if __name__ == '__main__':
    app1.run(debug=True)