#!/usr/bin/python3
"""Starts a Flask web application.
The application listens on 0.0.0.0, port 5000.
Routes:
    /hbnb: HBnB home page.
"""
from models import storage
from flask import Flask
fro__)


@app.route("/hbnb", strict_slashes=False)
dem flask import render_template

app = Flask(__namef hbnb():
    """Displays the main HBnB filters HTML page."""
    states = storage.all("State")
    amenities = storage.all("Amenity")
    places = storage.all("Place")
    return render_template("100tes, amenities=amenities, places=places)


@app.te-hbnb.html",
                           states=staardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
