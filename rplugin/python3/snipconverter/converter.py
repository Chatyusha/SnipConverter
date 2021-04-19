import re
from pathlib import Path
from snipconverter.util.reader import SnipConV
from snipconverter.util.format import Format

class Converter(object):
    def __init__(self):
#        self.snips_dir = snips_dir \
#                if re.search(r"/$",snips_dir) \
#                else snips_dir + r"/"
#        self.vsnips_dir = vsnips_dir \
#                if re.search(r"/$",vsnips_dir) \
#                else vsnips_dir + r"/"
        self.snip_conv = SnipConV()
        self.format = Format()
    
    def Snip2VSnip(self, input_filepath,output_dir):

        output_dir = output_dir \
                if re.search(r"/$",output_dir) \
                else output_dir + r"/"
        path = Path(input_filepath)
        filename = path.stem + ".json"
        SnipDict={}
        self.format.JsonFormat(self.snip_conv.Snip2VScode_dict(input_filepath,SnipDict),output_dir + filename)



