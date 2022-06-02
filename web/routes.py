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
    return flask.render_template("home.html", nav_page="home", splash=True)


@app.route("/project1")
def project1():
    return flask.render_template("empty-project.html", nav_page="project1")


@app.route("/project2")
def project2():
    return flask.render_template("empty-project.html", nav_page="project2")


@app.route("/project3")
def project3():
    return flask.render_template("empty-project.html", nav_page="project3")


@app.route("/project4")
def project4():
    return flask.render_template("empty-project.html", nav_page="project4")


@app.route("/project5")
def project5():
    return flask.render_template("empty-project.html", nav_page="project5")
