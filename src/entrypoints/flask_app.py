from flask import (
    Flask, request
)

import sys
sys.path.insert(1, '../../')
from src.services.hdfs_controller import HDFSController
from src.render.default_pages import Pages
from config import MainConfig

app = Flask(__name__, template_folder='../src/templates', static_folder='../src/static')
hdfs_controller = HDFSController()


@app.route('/')
def start():
    return Pages.start()

@app.route('/racks', methods=["POST"])
def get_hosts():
    req = request
    form = req.form
    path = form.get("path", default=None) or "/"
    if path[0] != "/":
        path = "/" + path
    if path:
        data = hdfs_controller.get_map(path) or "Ничего не удалось найти :("
        return Pages.show_racks(data, path=path)

    return "Empty form error!"


@app.route('/find', methods=["POST"])
def get_path():
    req = request
    form = req.form
    filename = form.get("filename", default=None)
    if filename:
        data = hdfs_controller.get_path(filename) or "Ничего не удалось найти :("
        return Pages.start(path=str(data))

    return Pages.start(err="Empty form error!")


@app.route('/folder', methods=["POST"])
def describe_folder():
    req = request
    form = req.form
    folder = form.get("folder", default=None).lstrip("/") or "/"
    if folder:
        data = hdfs_controller.describe_folder(folder) or "Ничего не удалось найти :("
        return Pages.show_hierarchy(data)

    return "Empty form error!"


if __name__ == '__main__':
    app.run(port=8000, host='0.0.0.0', debug=MainConfig.debug)
