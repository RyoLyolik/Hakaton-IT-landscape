from src.services.formatter import Formatter
from src.services.request_controller import RequestController
from src.services.ssh_controller import SSHController
class HDFSController:
    def __init__(self):
        self.sc = SSHController()
        self.sc.connect()
        self.rc = RequestController()

    def get_map(self, path: str):
        return Formatter.pull_out_file_blocks(self.rc.build_map(path))

    def get_path(self, filename: str):
        if self.sc.isalive():
            return self.sc.find_path(filename)
        self.sc.connect()
        if not self.sc.isalive():
            raise ConnectionError
        return self.get_path(filename)
