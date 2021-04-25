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
        self.vars = util.vars.Vars(nvim)
        self.converter = Converter()
        self.cache = CacheTimeStamps(self.plugin_path+ "/cache/cache.json")

    def vimecho(self,msg: str):
        self.nvim.command("echo \"" + msg + "\"")

    
    @pynvim.autocmd("VimEnter")
    def vimenter(self):
        if os.path.exists(self.plugin_path+"/cache") == False:
            self.vimecho("MakeCacheFolder")
            subprocess.run(['mkdir',self.plugin_path+'/cache'])
            with open(self.plugin_path + '/cache/cache.json','w') as f:
                f.write("{}")
        if self.vars.autload == 1:
            self.loadsnip()
            self.writecache()

    @pynvim.command('Dummy')
    def damy(self):
        self.nvim.command("echo \"" + str(self.vars.nvim.vars['snip_tabwidth']) + "\"")

    @pynvim.command('LoadSnip')
    def loadsnip(self): 
        for i in self.vars.snip_dirpath:
            self.cache.MakeCache(i,".snip")
        self.cache.LoadCache()
        diffs=self.cache.GetDiff()
        for i in diffs:
            self.vimecho(str(i))
            self.converter.Snip2VSnip(i,self.vars.vsnip_path)
        #self.vimecho(str(diffs))
        #self.vimecho("Make Cache file and Under Development")

    # Make Cache.json
    @pynvim.command('MakeSnipCache')
    def makesnipcache(self):
        for i in self.vars.snip_dirpath:
            self.cache.MakeCache(i,".snip")
    
    @pynvim.command('WriteCache')
    def writecache(self):
        self.cache.WriteCache()
    
    @pynvim.command("DeleteCache")
    def deletecache(self):
        subprocess.run(['rm',self.plugin_path + '/cache/cache.json'])
        with open(self.plugin_path + '/cache/cache.json','w') as f:
            print(subprocess.run(['echo','-n','{}'],encoding='utf-8',stdout=subprocess.PIPE).stdout,file=f)

    @pynvim.command("DeleteVsnipAll")
    def delete_vsnip_all(self):
        path = self.nvim.vars['vsnip_path']
        ls = subprocess.run(['/bin/ls','-a',path],encoding='utf-8',stdout=subprocess.PIPE).stdout.split("\n")[2:-1]
        #self.vimecho(str(ls))
        for i in ls:
            subprocess.run(['rm',path+i])
