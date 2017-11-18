#!/usr/bin/env python
from flask import Flask
import mad_libs

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
