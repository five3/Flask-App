import os
from flask import Blueprint, current_app, render_template, request
from {% project_name %}.apps.utils import get_abs_dir
from {% project_name %}.apps.utils.constants import METHODTYPE

index = Blueprint('index', __name__, url_prefix='/{% app_name %}/',
                  template_folder=os.path.join(get_abs_dir(__file__), '../templates'))


@index.route('/', methods=[METHODTYPE.GET, METHODTYPE.POST])
def index_home():
    current_app.logger.info(f'{request.method} for index.home')
    if request.method == METHODTYPE.GET:
        name = request.args.get('name', 'Python')
        return render_template('home.html', name=name)  # return html Content
    else:
        name = request.form.get('name', 'Python')   # for request that POST with application/x-www-form-urlencoded
        return f"Hello {name}", 200         # return plain text Content
