import json
from . import reader
from .reader import SnipConV

class Format(SnipConV):
    def JsonFormat(self, dic: dict,file_path: str):
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(dic, f, ensure_ascii=False, indent=4)

