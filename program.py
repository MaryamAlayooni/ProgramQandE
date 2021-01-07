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

program.config['SQLALCHEMY_DATABASE_URI']= 'program_db_users.sql'

#call the database
mysql = MySQL(program)

@app.route('/program_db/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', msg='Welcome')

def index():
    #check if the data in database
    if request.method == 'POST' and 'user_id' in request.form and 'user_pass' in request.form:
        user_id = request.form['user_id']
        uer_pass = request.form['user_pass']
#check on databse
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM users WHERE user_id = %s AND user_pass = %s', (user_id, user_pass))
        users = cursor.fetchone()

        if users:
            session['loggedin'] = True
            session['id'] = users['id']
            session['user_id'] = users['user_id']
            
            #<!--- determain admin/Regular----->

            return redirect(url_for(''))   
        else:
            msg= "Incorrect user id or password"

@app.route('/program_db/logout')  #-------------------- logout button!!!!
def logout():
   session.pop('loggedin', None)
   session.pop('id', None)
   session.pop('username', None)
   return redirect(url_for('index'))

@app.route('/program_db/Regular')
def Regular():
    if 'loggedin' in session:
        return render_template('Regular.html', username=session['username']) #------------------------- make sure of user name
    return redirect(url_for('index'))

@app.route('/program_db/Admin')
def Admin():
    if 'loggedin' in session:
        return render_template('Admin.html', username=session['username']) #------------------------- make sure of user name
    return redirect(url_for('index'))



"""class Users(db.Model):
    user_id=db.Column(db.Integer, primary_key=True)
    user_pass=db.Cloumn(db.varchar(10))
    user_name=db.Column(db.varchar(20))
    user_dep=db.Column(db.varchar(10))
    IsAdmin=db.Column(db.varchar(1)) """

""""-def User_Admin():
    if user_id and IsAdmin == 1 :
     return(Admin.html)
    else:
        return(Regular.html)"""

        
