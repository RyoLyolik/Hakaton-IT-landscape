import subprocess
from subprocess import PIPE
import re
import paramiko
import os

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

    def build_map(self, path):
        ssh_stdin, ssh_stdout, ssh_stderr = self.__client.exec_command(
            f"hdfs fsck {path} -files -locations -blocks -racks")
        data = ssh_stdout.readlines()
        # for i in range(len(data)):
        #     data[i] = data.strip()
        data = "".join(data)
        return data

    def disconnect(self):
        self.__client.close()

    def isalive(self):
        if self.__client.get_transport().is_alive():
            return True
        self.connect()
        return self.__client.get_transport().is_alive()

    def build_map_on_srv(self, path):
        data = subprocess.run(f"hdfs fsck {path} -files -locations -blocks -racks", shell=True, stdout=PIPE).stdout.decode('utf-8')
        return data

    def find_file_on_srv(self, filename):
        path = subprocess.run(f"hadoop fs -find {self.default_folder} -name {filename}", shell=True, stdout=PIPE).stdout.decode('utf-8')
        return path

    def folder_data_on_srv(self, folder):
        data = subprocess.run(f"sudo hadoop fs -find {self.default_folder + folder}", shell=True, stdout=PIPE).stdout.decode('utf-8')

        return data.split("\n")
