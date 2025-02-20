from flask import current_app as app
from flask import jsonify


@app.errorhandler(400)
def bad_request(e):
    return jsonify({
        "message": "Bad Request",
        "error": str(e)
        }), 400


@app.errorhandler(404)
def not_found(e):
    return jsonify({
        "message": "Not Found",
        "error": str(e)
        }), 404

@app.errorhandler(405)
def method_not_allowed(e):
    return jsonify({
        "message": "Method Not Allowed",
        "error": str(e)
        }), 405


@app.errorhandler(500)
def internal_server_error(e):
    return jsonify({
        "message": "Internal Server Error",
        "error": str(e)
        }), 500

