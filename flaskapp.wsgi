#!/usr/bin/python3
import sys

sys.path.insert(0, "/var/www/DigitalArtPortfolio/")

from flaskapp import app as application
from flaskapp import ENV
application.secret_key = ENV["secret_key"]
