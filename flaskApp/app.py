from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def data():  # put application's code here
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')
