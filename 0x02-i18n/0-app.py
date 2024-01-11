#!/usr/bin/env python3
"""Basic flask app"""

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index() -> str:
    """Handles a single / route"""
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(port="5000", host="0.0.0.0", debug=True)
