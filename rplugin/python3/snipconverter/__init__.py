import pynvim
from pathlib import Path
from snipconverter.util.vars import Vars
from snipconverter.converter import Converter

@pynvim.plugin
class SnipConverter(object):
    def __init__(self, nvim):
        self.nvim = nvim
        self.plugin_path = Path(__file__).parent.parent.parent.parent
        self.vsnip_dir = str(self.plugin_path) + r"/snippets/vsnip"
        self.snip_dir = str(self.plugin_path) + r"/snippets/snip"
        self.vars = util.vars.Vars(nvim)
        self.converter = Converter(vsnips_dir=)


    @pynvim.command('Damy')
    def damy(self):
        self.nvim.command("echo \"" + str(self.vars.nvim.vars['snip_tabwidth']) + "\"")

