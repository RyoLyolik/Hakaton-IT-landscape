from flask import (
    Flask, request
)

from src.services.hdfs_controller import HDFSController
from src.render.default_pages import Pages

app = Flask(__name__, template_folder='../src/templates', static_folder='../src/static')
hdfs_controller = HDFSController()

@app.route('/', methods=["GET", "POST"])
def start():
    req = request
    form = req.form
    path = form.get("path", default=None)
    filename = form.get("filename", default=None)
    if path:
        data = hdfs_controller.get_map(path)
        return str(data)
    if filename:
        data = hdfs_controller.get_path(filename)
        return str(data)
    return Pages.start()

if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1', debug=True)
