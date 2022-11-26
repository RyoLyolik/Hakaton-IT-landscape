from datetime import datetime
import flask

from request_controller import RequestController
from formatter import Formatter
from ssh_controller import SSHController

"""
/DATA/USDRUB_990801_201010.txt
/DATA/lenta-ru-news.csv
/DATA
"""

rc = RequestController()
sc = SSHController()
fmt = Formatter()
start = datetime.now()
text = rc.build_map("/DATA/lenta-ru-news.csv")
end = datetime.now()
print(end-start)
blocks = fmt.pull_out_file_blocks(text)
print(blocks)
