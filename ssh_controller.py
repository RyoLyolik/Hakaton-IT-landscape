import subprocess
import re
import paramiko
class SSHController:
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname="10.129.0.162", username="admin", password="adb@2015", port=22)
    ssh_stdin, ssh_stdout, ssh_stderr = client.exec_command("hdfs fsck /DATA/ -files -blocks -racks")
    opt = ssh_stdout.readlines()
    opt = "".join(opt)
    opt1=re.findall("\[([^\[\]]*)\]",opt)[0]
    opt2=opt1.split(", ")
    print(opt2)
    client.close()
