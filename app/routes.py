from flask import render_template, request, render_template_string

from app import app

messages = []


@app.route("/")
def index():
    return render_template("index.html", messages=messages, title="GrandPy Bot")
