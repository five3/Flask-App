from flask import Blueprint, jsonify, current_app

index = Blueprint('index', __name__, url_prefix='/')


@index.route('/')
def home():
    current_app.logger.info('index.home')
    return jsonify({"success": True, "name": 'index.home'})
