import pynvim
from snipconverter.util.vars import Vars

@pynvim.plugin
class SnipConverter(object):
    def __init__(self, nvim):
        self.nvim = nvim
        self.vars = util.vars.Vars(nvim)

    @pynvim.command('Damy')
    def damy(self):
        self.nvim.command("echo \"" + str(self.vars.nvim.vars['snip_tabwidth']) + "\"")

