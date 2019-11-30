from flask import Blueprint, jsonify, current_app

datasource = Blueprint('datasource', __name__, url_prefix='/datasource')


@datasource.route('/')
def ds_index():
    current_app.logger.info('ds.index')
    return jsonify({"success": True, "name": 'ds.index'})
