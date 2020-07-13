from flask import render_template, request

from app import app

import json


@app.route("/")
def index():
    return render_template("index.html", title="GrandPy Bot")


@app.route("/search", methods=["POST"])
def search():
    return request.form["s"]
