import os

from flask import jsonify, render_template, request

from app import app
from app.address_parser import AddressMatchNotFound, Parser
from app.maps import Maps
from app.mediawiki import MediaWiki


@app.route("/")
def index():
    API_KEY = os.environ["GOOGLE_MAPS_API_KEY"]
    return render_template("index.html", title="GrandPy Bot", key=API_KEY)


@app.route("/search", methods=["POST"])
def search():
    # Initialize an object to parse the data sent in form
    message = request.form["input_message"]
    # Get the main place keyword
    try:
        place = Parser.address_parser(message)
    except AddressMatchNotFound:
        return jsonify({"error": "Désolé, tu peux reformuler ta question..."})

    # Call Google Maps API
    location = Maps().get_maps_information(place)

    if location is not None:
        address = location["formatted_address"]
        lat = location["lat"]
        lng = location["lng"]
        # Call MediaWiki API
        wiki_extract = MediaWiki().get_mediawiki_information(lat, lng)
    else:
        address, lat, lng, wiki_extract = None, None, None, None
        
    # Dictionary in response to the ajax request
    response = {
        "address": address,
        "lng": lng,
        "lat": lat,
        "wiki_extract": wiki_extract
    }
    return jsonify(response)
