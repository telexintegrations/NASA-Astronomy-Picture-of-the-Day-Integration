import json
from concurrent.futures import ThreadPoolExecutor

import requests
from flask import Response, jsonify, request
from flask_restful import Resource

from .. import config
from ..utilities.apod_manager import APODManager, trigger_tick


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
            settings['data']['tick_url'] = f"{config.app_url}/napod-tick"

        return jsonify(settings), 200

    @staticmethod
    def tick():
        print("running tick")
        if request.method == 'POST':
            print(request.json)
            url = request.json.get('return_url', "https://ping.telex.im/v1/webhooks/01952fda-3658-7ddb-aa06-af3cb2462c3d")
        else:
            url = "https://ping.telex.im/v1/webhooks/01952fda-3658-7ddb-aa06-af3cb2462c3d"

        executor = ThreadPoolExecutor(max_workers=1)
        executor.submit(trigger_tick, url)

        response = {'status': 'accepted'}
        print(response)

        return jsonify({'status': 'accepted'}), 202

    @staticmethod
    def target():
        print("running target")
        print(request.json)

        response_data = {
            "event_name": "NAPOD Target",
            "message": f"Hello From NAPOD",
            "status": "success",
            "username": "NAPOD"
        }
        return jsonify(response_data), 200

    @staticmethod
    def get_apod():
        apod_manager = APODManager()
        return apod_manager.get_apod()
