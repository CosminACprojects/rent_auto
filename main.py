from database_management import *
from flask import Flask,render_template,redirect


#app=Flask(__name__)

#@app.route('/')
#def home():
#    return render_template('home.html',text='SUNT BOSS')

create_tables_and_constraints()
