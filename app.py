from flask import Flask, request, render_template, current_app as app
from sense_hat import SenseHat
import sqlite3
import requests

#sense = SenseHat()

app = Flask(__name__)

@app.route('/')
def index():
    request.method == 'POST'
    return render_template('index.html')

@app.route('/welcome', methods=['GET','POST'])
def welcome():
    response = requests.get('https://zenquotes.io/api/random') 
    #(.)means theres a variable. response is a variable that i create not native to python
    data = response.json()
    print (data)
    return render_template('welcome.html', data = data)

@app.route('/all')
def all():
    # happy = request.form['happy']
    # sense.show_message(happy)
    # sad = request.form['sad']
    # sense.show_message(sad)
    # okay = request.form['okay(neutral)']
    # sense.show_message(neutral)
    # tired = request.form['tired/exhausted']
    # sense.show_message(tired/exhausted)
    #those lines dont work but idk how to trigger the buttons to send info to the database
    #i tried to use javascript but i think that its not working bc there are 4 separate buttons for one db column
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