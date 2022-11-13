#!/usr/bin/python3
"""Starts a Flask web application.
The application listens on 0.0.0.0, port 5000.
Routes:
    /states: HTML page with a list of all State objects.
    /states/<id>: HTML page displaying the given state with <id>.
"""
from models import storage
from flask import Flask
from fl

@app.route("/states", strict_slashes=False)
def ask import render_template

app = Flask(__name__)
states():
    """Displays an HTML page with a list of all States.
    States are sorted by name.
    """
    states = storage.all("State")
    return render_template("9-states.html", state=states)


@f states_id(id):
    """Displays an HTML page withapp.route("/states/<id>", strict_slashes=False)
de info about <id>, if it exists."""
    for state in storage.all("State").values():
        if state.ates.html", state=state)
    return render_templatid == id:
            return render_template("9-ste("9-states.html")


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
