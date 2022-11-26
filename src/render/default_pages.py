from flask import render_template
import subprocess
import os
class Pages:
    @staticmethod
    def start():
        return render_template('index.html')

    @staticmethod
    def show_racks():
        return render_template('racks.html')