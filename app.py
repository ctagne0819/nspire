from flask import Flask, request, render_template, current_app as app
from sense_hat import SenseHat
#from flask_apscheduler import APScheduler
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    request.method == 'POST'
    return render_template('index.html')

@app.route('/welcome', methods=['GET','POST'])
def welcome():
    return render_template('welcome.html')

@app.route('/all')
def all():
    conn = sqlite3.connect('./static/data/nspire.db')
    curs = conn.cursor()
    userInput = []
    rows = curs.execute("SELECT * from userInput")
    for row in rows:
        mood = {'mood': row[1], 'timestamp': row[2]}
        userInput.append(mood)
    conn.close()
    return render_template('all.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0') 