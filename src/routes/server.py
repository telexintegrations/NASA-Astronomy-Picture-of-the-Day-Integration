""" 
server.py

Route for server
"""
from flask import Blueprint

from ..resources import ServerResource

ServerBlueprint = Blueprint("server", __name__)

ServerBlueprint.route('/healthcheck', methods=["GET"])(ServerResource.healthcheck)
ServerBlueprint.route('/integration.json', methods=["GET", "POST"])(ServerResource.integration_settings)
ServerBlueprint.route('/tick', methods=["GET", "POST"])(ServerResource.tick)
ServerBlueprint.route('/target', methods=["GET", "POST"])(ServerResource.target)
ServerBlueprint.route('/apod', methods=["GET"])(ServerResource.get_apod)