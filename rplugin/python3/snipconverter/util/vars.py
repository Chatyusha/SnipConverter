import pynvim

class Vars(object):
    def __init__(self,nvim):
        self.nvim = nvim
        self.nvim.vars['snip_tabwidth'] = 4
        self.nvim.vars['snip_tabstop'] = 4

