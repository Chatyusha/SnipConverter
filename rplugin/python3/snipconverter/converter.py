import os
import re
from util.reader import SnipConV
from util.format import Format

class Converter(object):
    def __init__(self,vsnips_dir: str, snips_dir: str):
        self.snips_dir = snips_dir \
                if re.search(r"/$",snips_dir) \
                else snips_dir + r"/"
        self.vsnips_dir = vsnips_dir \
                if re.search(r"/$",vsnips_dir) \
                else vsnips_dir + r"/"
        self.snip_conv = SnipConV()
        self.format = Format()

    def Snip2VSnip(self,file_name: str):
        input_file_path = self.snips_dir + file_name
        basename = os.path.splitext(os.path.basename(input_file_path))[0]
        output_file_path = self.vsnips_dir + basename + r".json"
        self.format.JsonFormat(self.snip_conv.Snip2VScode_dict(input_file_path),
                output_file_path)



