import os
import flask
import traceback
from web import app


@app.errorhandler(500)
def internal_server_error(_):
    error = traceback.format_exc()
    return flask.render_template("500.html", title="Error", error=error)


@app.errorhandler(404)
def internal_server_error(_):
    return flask.render_template("404.html", title="Page Not Found")


@app.route("/")
def home():
    return flask.render_template("general/home.html", title="Home")
