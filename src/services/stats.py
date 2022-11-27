from ssh_controller import SSHController
from request_controller import RequestController
from datetime import datetime

sc = SSHController()
rc = RequestController()

sc.connect()
ssh_start = datetime.now()
ssh_answer = sc.build_map("/DATA/USDRUB_990801_201010.txt")
ssh_end = datetime.now()

req_start = datetime.now()
request_answer = rc.build_map("/DATA/USDRUB_990801_201010.txt")
req_end = datetime.now()

print("SSH:", ssh_end-ssh_start)
print("Request:", req_end-req_start)

sc.disconnect()
