from flask import Blueprint, jsonify

index = Blueprint('index', __name__, url_prefix='/')


@index.route('/')
def home():
    return jsonify({"success": True, "name": 'index.home'})
