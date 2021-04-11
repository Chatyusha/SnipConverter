from pathlib import Path
import json
import subprocess

class CacheTimeStamps:

    def __init__(self,cachefile):
        self.cache={}

    def MakeCache(self,path):

