#!/usr/bin/env python3
'''flak app'''
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def welcome():
    '''web page rendering'''
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
