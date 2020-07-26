import os

from flask import jsonify, render_template, request

from app import app
from app.address_parser import AddressMatchNotFound, Parser
from app.maps import Maps
from app.mediawiki import MediaWiki
from app.sentences import Sentences


@app.route("/")
def index():
    API_KEY = os.environ["GOOGLE_MAPS_API_KEY"]
    return render_template("index.html", title="GrandPy Bot", key=API_KEY)


@app.route("/search", methods=["POST"])
def search():
    # Initialize an object to parse the data sent in form
    message = request.form["input_message"]

    sentence, wiki_sentence = Sentences.get_sentences()
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

        address_reply = sentence + address
        wiki_reply = wiki_sentence + wiki_extract
    else:
        address, lat, lng = None, None, None
        address_reply = "Oops, je crois que ce lieu est imaginaire..."
        wiki_reply = None

    # Dictionary in response to the ajax request
    response = {
        "address_reply": address_reply,
        "address": address,
        "lng": lng,
        "lat": lat,
        "wiki_reply": wiki_reply
    }
    return jsonify(response)
