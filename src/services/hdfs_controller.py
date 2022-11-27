from src.services.formatter import Formatter
from src.services.request_controller import RequestController
from src.services.ssh_controller import SSHController
from config import MainConfig


class HDFSController:
    def __init__(self):
        self.sc = SSHController()
        self.sc.connect()
        self.rc = RequestController()

    def get_map(self, path: str):
        if MainConfig.debug:
            return Formatter.hosts_to_dict(Formatter.pull_out_file_hosts(self.rc.build_map(path)))
        return Formatter.hosts_to_dict(Formatter.pull_out_file_hosts(self.sc.build_map_on_srv(path)))

    def get_path(self, filename: str):
        if MainConfig.debug:
            if self.sc.isalive():
                return self.sc.find_path(filename)
            else:
                raise ConnectionError
        return self.sc.find_file_on_srv(filename)

    def describe_folder(self, path):
        if MainConfig.debug:
            if self.sc.isalive():
                tree = Formatter.numerate_folder(self.sc.folder_data(path))
                return tree
            else:
                raise ConnectionError

        return Formatter.numerate_folder(self.sc.folder_data_on_srv(path))
