from flask import render_template
import subprocess
import os


class Pages:
    @staticmethod
    def start(path=str(), err=None):
        return render_template('index.html', path=path, error=err)

    @staticmethod
    def show_racks(racks=dict(), path="/"):
        if not isinstance(racks, dict):
            racks = dict()
        i = 0
        for rack in racks:
            for j, host in enumerate(racks[rack]):
                id_host = dict()
                id_host["id"] = "id" + str(i)
                id_host["host"] = host
                racks[rack][j] = id_host
                i += 1
        return render_template('racks.html', racks=racks, path=path)

    @staticmethod
    def show_hierarchy(folder_desc=list()):
        if not isinstance(folder_desc, list):
            folder_desc = [folder_desc]

        folders = list()
        for i, folder in enumerate(folder_desc):
            folders.append(
                {
                    "id": "id" + str(i),
                    "path": folder
                }
            )
        return render_template('hierarchy.html', folders=folders)
