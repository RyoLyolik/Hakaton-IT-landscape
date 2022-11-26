import subprocess
import re
import paramiko
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname="10.129.0.162", username="admin", password="adb@2015", port=22)
name=input()
stdin, stdout, stderr = client.exec_command(f"hadoop fs -find / -name {name}")
opt1 = stdout.readlines()
opt1 = "".join(opt1).strip()
print(opt1)
ssh_stdin, ssh_stdout, ssh_stderr = client.exec_command(f"hdfs fsck {opt1} -files -locations -blocks -racks")
opt = ssh_stdout.readlines()
opt = "".join(opt)
print(opt)
opt3=re.findall("\[([^\[\]]*)\]",opt)
print(opt3)
client.close()

