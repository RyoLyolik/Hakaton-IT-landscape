from flask import render_template


class Pages:
    @staticmethod
    def start(path=str(), err=None):
        return render_template('index.html', path=path, error=err, title="Start")

    @staticmethod
    def show_racks(racks=dict(), path="/"):
        if not isinstance(racks, dict):
            racks = dict()
        return render_template('racks.html', racks=racks, path=path, title="Racks")

    @staticmethod
    def show_hierarchy(folders=list()):
        if not isinstance(folders, list):
            folders = []
        return render_template('hierarchy.html', folders=folders, title="Hierarchy")
