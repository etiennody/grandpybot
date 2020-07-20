import os

from flask import jsonify, render_template, request

from app import app
from app.address_parser import Parser
from app.maps import Maps


@app.route("/")
def index():
    API_KEY = os.environ["GOOGLE_MAPS_API_KEY"]
    return render_template("index.html", title="GrandPy Bot", key=API_KEY)


@app.route("/search", methods=["POST"])
def search():
    # Initialize an object to parse the data sent in form
    message = request.form["input_message"]
    # Get the main place keyword
    place = Parser.address_parser(message)
    # Call Google Maps API
    location = Maps().get_maps_information(place)

    if location is not None:
        address = location["formatted_address"]
        lat = location["lat"]
        lng = location["lng"]

    else:
        address, lat, lng = None, None, None

    # Dictionary in response to the ajax request
    response = {
        "address": address,
        "lng": lng,
        "lat": lat,
    }
    return jsonify(response)
