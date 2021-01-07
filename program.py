from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import flask_SQLAlchemy
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re


program = Flask(__name__)

#database connection
program.config['MYSQL_HOST'] = 'localhost'
program.config['MYSQL_USER'] = 'root'
program.config['MYSQL_PASSWORD'] = ''
program.config['MYSQL_DB'] = 'program_db'
#to skip any error may occure
program.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

program.config['SQLALCHEMY_DATABASE_URI']= 'program_db.sql'

#call the database
mysql = MySQL(program)

@app.route('/program_db/', methods=['GET', 'POST'])

 def index():
    return render_template('index.html', msg='Welcome')

 def index():
    #check if the data in database
    if request.method == 'POST' and 'user_id' in request.form and 'user_pass' in request.form:
        user_id = request.form['user_id']
        user_pass = request.form['user_pass']
#check on databse
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM users WHERE user_id = %s AND user_pass = %s', (user_id, user_pass))
        users = cursor.fetchone()

#check the autherity 
        if users:
            session['loggedin'] = True
            session['id'] = users['user_id'], user_id.find("A")
            session['id'] = users['user_pass']
            return redirect(url_for('Admin.html'))   
        elif users:
            session['loggedin'] = True
            session['id'] = users['user_id'], user_id.find("U")
            session['id'] = users['user_pass']
            return redirect(url_for('Regular.html')) 
        else:

            print=("Incorrect user id or password")

        
