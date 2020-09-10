# import json
import os

from flask import Flask, send_from_directory
# from models import init_db

from controller import VideoController


class CustomFlask(Flask):
    jinja_options = Flask.jinja_options.copy()
    jinja_options.update(dict(
        block_start_string='<%',
        block_end_string='%>',
        variable_start_string='%%',
        variable_end_string='%%',
        comment_start_string='<#',
        comment_end_string='#>',
    ))


PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

path = '.\\db'
app = CustomFlask(__name__, template_folder='../web_templates',
                  static_folder='../static')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../db/DataBase.sqlite'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['UPLOAD_FOLDER'] = os.path.join(PROJECT_ROOT, '..', 'data')
# app.config['DATABASE_FOLDER'] = os.path.join(PROJECT_ROOT, '..', 'db')
# app.config['MEDIA_ROOT'] = os.path.join(PROJECT_ROOT, 'media_files')

# Confiiguração das rodas de forma modular
app.register_blueprint(VideoController.router, url_prefix='/')


@app.route('/node_modules/<path:path>')
def send_js(path):
    return send_from_directory('../node_modules/', path, as_attachment=True, mimetype='application/javascript')


@app.route('/video_process/<path:path>')
def send_web_app(path):
    return send_from_directory('../video_process/', path, as_attachment=True, mimetype='application/octet-stream')


def _init():
    # global data
    # return init_db(app)
    print('not implemented')


if __name__ == "src.app":
    _init()

if __name__ == "__main__":
    _init()
    app.run(host='0.0.0.0', port=80, debug=True, use_reloader=True)
