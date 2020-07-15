from flask import jsonify, render_template, request

from app import app
from app.address_parser import Parser


@app.route("/")
def index():
    return render_template("index.html", title="GrandPy Bot")


@app.route("/search", methods=["POST"])
def search():
    message = request.form["message"]
    fulfillment_text = Parser.address_parser(message)
    response_text = {"message": fulfillment_text}
    return jsonify(response_text)
