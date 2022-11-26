import re


class Formatter:
    @staticmethod
    def pull_out_file_blocks(text):
        blocks_texts = re.findall(r'\[([^\[\]]*)\]', text)
        blocks = set()
        for block_text in blocks_texts:
            block_hosts = block_text.split(', ')
            for host in block_hosts:
                blocks.add(host)
        return blocks
