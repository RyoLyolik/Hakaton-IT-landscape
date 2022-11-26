from src.services.formatter import Formatter
from src.services.request_controller import RequestController
from src.services.ssh_controller import SSHController


class HDFSController:
    def __init__(self):
        self.sc = SSHController()
        self.sc.connect()
        self.rc = RequestController()

    def get_map(self, path: str):
        return Formatter.hosts_to_dict(Formatter.pull_out_file_hosts(self.rc.build_map(path)))

    def get_path(self, filename: str):
        if self.sc.isalive():
            return self.sc.find_path(filename)
        else:
            raise ConnectionError

    def describe_folder(self, path):
        if self.sc.isalive():
            tree = self.sc.folder_data(path)
            return tree
        else:
            raise ConnectionError
