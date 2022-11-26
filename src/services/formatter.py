import re


class Formatter:
    @staticmethod
    def pull_out_file_hosts(text):
        blocks_texts = re.findall(r'\[([^\[\]]*)\]', text)
        hosts = set()
        for block_text in blocks_texts:
            block_hosts = block_text.split(', ')
            for host in block_hosts:
                hosts.add(host)
        return hosts

    @staticmethod
    def hosts_to_dict(hosts: set):
        racks = dict()
        for host_text in hosts:
            sep_index = re.search("(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5})", host_text).span()[0]
            rack, host = host_text[:sep_index], host_text[sep_index:]
            if rack in racks:
                racks[rack].append(host)
            else:
                racks[rack] = [host]
        return racks

# if __name__ == "__main__":
#     from request_controller import RequestController
#     import re
#
#     rc = RequestController()
#     path = "/DATA/lenta-ru-news.csv"
#     # path = "/DATA/USDRUB_990801_201010.txt"
#     txt = rc.build_map(path)
#     map = Formatter.pull_out_file_hosts(txt)
#     print(map)
#     racks = dict()
#     for host_text in map:
#         sep_index = re.search("(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5})", host_text).span()[0]
#         rack, host = host_text[:sep_index], host_text[sep_index:]
#         print(rack, host)
#         if rack in racks:
#             racks[rack].append(host)
#         else:
#             racks[rack] = [host]
#
#     print(racks)
