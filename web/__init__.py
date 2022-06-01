import os
import json
from flask import Flask

from web import startup_utils
from web.common import from_root

# System Files
VARIABLES_FILE = from_root(os.pardir, "flask_env.json")


startup_utils.generate_app_structure()

with open(VARIABLES_FILE) as var_file:
    ENV = json.load(var_file)
app = Flask(__name__)
app.config["SECRET_KEY"] = ENV["secret_key"]

from web import routes


def start(debug=False):
    if debug:
        app.run(debug=True, host='0.0.0.0')
    else:
        app.run()


if __name__ == "__main__":
    start()

