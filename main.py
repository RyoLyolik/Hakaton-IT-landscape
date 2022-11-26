from request_controller import RequestController
from formatter import Formatter

"""
/DATA/USDRUB_990801_201010.txt
/DATA/lenta-ru-news.csv
/DATA
"""

rc = RequestController()
fmt = Formatter()
text = rc.build_map("/DATA/lenta-ru-news.csv")
blocks = fmt.pull_out_file_blocks(text)
print(blocks)
