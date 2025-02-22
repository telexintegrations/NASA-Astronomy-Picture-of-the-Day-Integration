import json

import requests
from flask import Response, jsonify, request
from flask_restful import Resource

from .. import config
from ..utilities.apod_manager import APODManager


class ServerResource(Resource):

    @staticmethod
    def healthcheck():
        return jsonify({"status": "Server is running"}), 200

    @staticmethod
    def integration_settings():
        print("calling integration settings")
        
        with open('integration_settings.json', 'r') as f:
            settings = json.load(f)
            settings['data']['target_url'] = f"{config.app_url}/target"
            settings['data']['tick_url'] = f"{config.app_url}/tick"

        return jsonify(settings), 200
    
    @staticmethod
    def tick():
        print("running tick")
        # print(request.json)

        url = "https://ping.telex.im/v1/webhooks/01951da5-750a-74c1-befc-559a5a88785e"
        # payload = {
        #     "event_name": "Daily Post",
        #     "message": "Hello From NAPOD",
        #     "status": "success",
        #     "username": "NAPOD"
        # }

        # response = requests.post(
        #     url,
        #     json=payload,
        #     headers={
        #         "Accept": "application/json",
        #         "Content-Type": "application/json"
        #     }
        # )
        response = {'status': 'accepted'}
        print(response)
        
        return jsonify(response), 202

    @staticmethod
    def target():
        print("running target")
        print(request.json)
        response_data = {
            "message": "message",
            "settings": [
                {
                "label": "setting_label",
                "type": "text",
                "default": "setting_value",
                "required": True
                    }
                ]
            }
        response_data = {
                "event_name": "message_formatted",
                "message": "Hello, world world. I hope you are happy happy today",
                "status": "success",
                "username": "message-formatter-bot"
            }
        return jsonify(response_data), 202
    
    @staticmethod
    def get_apod():
        apod_manager = APODManager()
        return apod_manager.get_apod()