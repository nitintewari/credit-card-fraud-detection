from flask import Flask, render_template, request
import pickle
import numpy as np
model = pickle.load(open('Class.pkl', 'rb'))
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    Time = request.form['time']
    Amount = request.form['amount']
    total = [[int(Time), int(Amount)]]
    y_pred = model.predict(total)

    if y_pred==1:
        msg='This transaction seems to be fraudulent. We request you to report it at http://www.cybercelldelhi.in/'
    else:
        msg='This transaction is not fraudulent!'
    return render_template("index.html", showcase = msg)


if __name__ == '__main__':
    app.run(debug=True)
