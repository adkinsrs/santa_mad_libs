#!/usr/bin/env python
from flask import Flask
from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired
import mad_libs

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

### Non-routing functions

def choose_random_mad_lib():
    pass

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
