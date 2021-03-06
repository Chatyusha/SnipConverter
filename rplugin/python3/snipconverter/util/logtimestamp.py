from pathlib import Path
import json
import subprocess
import re

class CacheTimeStamps:

    def __init__(self,cachefile):
        self.cache={}
        self.loaded={}
        self.cachefile = cachefile

    def MakeCache(self,path,suffix):
        cp = subprocess.run(['ls', '-1F',path],encoding='utf-8',stdout=subprocess.PIPE)
        lsList = cp.stdout.split("\n")[:-1]
        for i in lsList:
            if re.search(r"/$",i):
                child = subprocess.run(['ls','-1F',path+i],encoding='utf-8',stdout=subprocess.PIPE).stdout.split("\n")[:-1]
                self.MakeCache(path+i,".snip")
            elif Path(i).suffix == ".snip":
                timestamp = subprocess.run(['date','+%Y-%m%d-%H%M%S','-r',path+i],encoding='utf-8',stdout=subprocess.PIPE).stdout[:-1]
                self.cache[path+i] = timestamp

    def WriteCache(self):
        with open(self.cachefile,"w",encoding='utf-8') as f:
            json.dump(self.cache,f,ensure_ascii=False,indent=4)

    def LoadCache(self):
        with open(self.cachefile) as f:
            self.loaded = json.load(f)

    def GetDiff(self):
        kesy = self.cache.keys()
        diffList = []
        for i in kesy:
            try:
                if self.cache[i] != self.loaded[i]:
                    diffList.append(i)
            except:
                diffList.append(i)
        return diffList

