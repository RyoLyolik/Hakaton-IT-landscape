import subprocess
import re
import paramiko

from config import SSHConfig


class SSHController:
    def __init__(self):
        self.hostname = SSHConfig.main_host
        self.default_port = SSHConfig.default_port
        self.username = SSHConfig.username
        self.default_folder = SSHConfig.default_folder
        self.__password = SSHConfig.password
        self.__client = paramiko.SSHClient()

        self.__client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def connect(self):
        self.__client.connect(hostname=self.hostname, username=self.username, password=self.__password,
                              port=self.default_port)

    def find_path(self, filename):
        stdin, stdout, stderr = self.__client.exec_command(f"hadoop fs -find {self.default_folder} -name {filename}")
        path = stdout.readlines()
        path = "".join(path).strip()

        return path

    def folder_data(self, folder):
        stdin, stdout, stderr = self.__client.exec_command(f"hadoop fs -find {self.default_folder + folder}")
        path = list()
        for out in stdout:
            path.append(out.strip())

        return path

    def disconnect(self):
        self.__client.close()

    def isalive(self):
        if self.__client.get_transport().is_alive():
            return True
        self.connect()
        return self.__client.get_transport().is_alive()
