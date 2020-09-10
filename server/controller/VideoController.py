from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

router = Blueprint(name='video_controller', import_name=__name__)


@router.route('/')
@router.route('/index')
def index():
    try:
        return render_template('Video/index.html')
    except TemplateNotFound:
        abort(404)
