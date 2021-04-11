import os
import re
from snipconverter.util.reader import SnipConV
from snipconverter.util.format import Format

class Converter(object):
    def __init__(self,vsnips_dir: str, snips_dir: str):
#        self.snips_dir = snips_dir \
#                if re.search(r"/$",snips_dir) \
#                else snips_dir + r"/"
#        self.vsnips_dir = vsnips_dir \
#                if re.search(r"/$",vsnips_dir) \
#                else vsnips_dir + r"/"
        self.snip_conv = SnipConV()
        self.format = Format()
    
    def Snip2VSnip(self, input_dir: str, output_dir: str, file_name: str):

        input_dir = input_dir \
                if re.search(r"/$",input_dir) \
                else input_dir + r"/"

        output_dir = output_dir \
                if re.search(r"/$",output_dir) \
                else output_dir + r"/"

        input_file_path = input_dir + file_name
        basename = os.path.splitext(os.path.basename(input_file_path))[0]
        output_file_path = output_dir + basename + r".json"
        self.format.JsonFormat(self.snip_conv.Snip2VScode_dict(input_file_path),
                output_file_path)



