from flask import Blueprint, jsonify, current_app, request, abort
from flask_app.apps.utils.constants import METHODTYPE

api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/', methods=[METHODTYPE.GET, METHODTYPE.POST])
def api_index():
    current_app.logger.info(f'{request.method} api.index')
    if request.method == METHODTYPE.GET:
        data = request.args
        return jsonify({"success": True, "name": 'api.index', 'data': data})
    else:
        data = request.json     # for request that POST with application/json
        return jsonify({"success": True, "name": 'api.index', 'data': data})


@api.route('/upload', methods=[METHODTYPE.POST])
def api_upload():
    current_app.logger.info(f'{request.method} api.upload')
    if request.method == METHODTYPE.GET:
        abort(405)

    files = request.files       # for request that POST with multipart/form-data's files
    data = request.form         # for request that POST with multipart/form-data's data
    return jsonify({"success": True, "name": 'api.upload', 'data': data, 'files': files})
