import pynvim
import os
from pathlib import Path
import subprocess
from snipconverter.util.vars import Vars
from snipconverter.util.logtimestamp import CacheTimeStamps
from snipconverter.converter import Converter

@pynvim.plugin
class SnipConverter(object):
    def __init__(self, nvim):
        self.nvim = nvim
        self.plugin_path = str(Path(__file__).parent.parent.parent.parent)
        self.vsnip_dir = self.plugin_path + r"/snippets/vsnip"
        self.snip_dir = self.plugin_path + r"/snippets/snip"
        self.vars = util.vars.Vars(nvim)
        self.converter = Converter(vsnips_dir=self.vsnip_dir,snips_dir=self.snip_dir)
        self.cache = CacheTimeStamps(self.plugin_path+ "/cache/cache.json")

    def vimecho(self,msg: str):
        self.nvim.command("echo \"" + msg + "\"")

    
    @pynvim.autocmd("VimEnter")
    def vimenter(self):
        if os.path.exists(self.plugin_path+"/cache") == False:
            self.vimecho("MakeCacheFolder")
            subprocess.run(['mkdir',self.plugin_path+'/cache'])

    @pynvim.command('Dummy')
    def damy(self):
        self.nvim.command("echo \"" + str(self.vars.nvim.vars['snip_tabwidth']) + "\"")

    @pynvim.command('LoadSnip')
    def custom_load_snip(self):
        self.vimecho("Under Development")

    @pynvim.command('MakeSnipCache')
    def makesnipcache(self):
        self.vimecho("Under Development")
#        for i in vars.snip_dirpath:
#            self.cache.MakeCache(i,"snip")
#        self.cache.WriteCache()
        
