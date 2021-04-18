import pynvim

class Vars(object):
    def __init__(self,nvim):
        self.nvim = nvim
        self.nvim.vars['snip_tabwidth'] = 4
        self.nvim.vars['snip_tabstop'] = 4
        self.snip_dirpath = self.nvim.vars['snip_dirpath']
        self.vsnip_path = self.nvim.vars['vsnip_path']
        self.autload = self.nvim.vars['snipconv_autoload']
