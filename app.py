from flask import Flask, render_template, request, current_app as current_app
from sense_hat import SenseHat
import sqlite3
from flask_apscheduler import APScheduler



@app.route('/all')
def all():
    conn = sqlite3.connect('./static/data/nspire.db')
    curs = conn.cursor()
    userInputs = []
    rows = curs.execute("SELECT * from userInputs")
    for row in rows:
        mood = {'mood': row[0], 'timestamp': row[1]}
        userInputs.append(mood)
    conn.close()
    return render_template('all.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0') 