""" 
server.py

Route for server
"""
from flask import Blueprint

from ..resources import ServerResource

ServerBlueprint = Blueprint("server", __name__)

ServerBlueprint.route('/healthcheck', methods=["GET"])(ServerResource.healthcheck)
ServerBlueprint.route('/integration.json', methods=["POST", "GET"])(ServerResource.integration_settings)
ServerBlueprint.route('/napod-tick', methods=["POST", "GET"])(ServerResource.tick)
ServerBlueprint.route('/tick', methods=["POST", "GET"])(ServerResource.tick)
ServerBlueprint.route('/target', methods=["POST", "GET"])(ServerResource.target)
ServerBlueprint.route('/apod', methods=["GET"])(ServerResource.get_apod)