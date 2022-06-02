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
    return flask.render_template("empty-project.html", nav_page="projects")


@app.route("/project2")
def project2():
    return flask.render_template("empty-project.html", nav_page="projects")


@app.route("/project3")
def project3():
    return flask.render_template("empty-project.html", nav_page="projects")


@app.route("/project4")
def project4():
    return flask.render_template("empty-project.html", nav_page="projects")


@app.route("/project5")
def project5():
    return flask.render_template("empty-project.html", nav_page="projects")


@app.route("/statements")
def statements():
    return flask.render_template("statements.html", nav_page="statements")


@app.route("/reflections")
def reflections():
    return flask.render_template("reflections.html", nav_page="reflections")
