from flask import Blueprint, jsonify

datasource = Blueprint('datasource', __name__, url_prefix='/datasource')


@datasource.route('/')
def ds_index():
    return jsonify({"success": True, "name": 'ds.index'})
