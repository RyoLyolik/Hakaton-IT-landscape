import requests

from config import Config


class RequestController:
    def __init__(self):
        self.available_hosts = Config.available_hosts
        self.default_port = Config.default_port

    def build_map(self, path):
        for i, host in enumerate(self.available_hosts):
            try:
                req = requests.get(
                    f'http://{host}:{self.default_port}/fsck',
                    params={
                        "ugi": "admin",
                        "files": 1,
                        "blocks": 1,
                        "racks": 1,
                        "path": path
                    }
                )
                self.available_hosts[0], self.available_hosts[i] = self.available_hosts[i], self.available_hosts[0]
                data = req.text
                return data
            except requests.exceptions.ConnectionError:
                pass
