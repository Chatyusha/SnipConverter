import re
import json

class SnipConV(object):
    class KeyWords:
        def __init__(self):
            self.include = r"^include"
            self.comment = r"^#"
            self.snippet = r"^snippet"
            self.options = r"^options"
            self.abbr = r"^abbr"
            self.alias = r"^alias"
            self.delete = r"^delete"
            self.tabspace = r"^  "
            self.tab = r"^(\t| )"
            self.empty = r"^\n"
    
    def __init__(self):
        self.kwds = SnipConV.KeyWords()
        self.imports = []
        self.name = ""
        self.indent=""
        self.snip_width=2
        self.snip_tabstop=2
        """
        {
            "SnipName":{
                "prefix":[snippet, aliases ...],
                "body":[
                    "......",
                    "......."
                ],
            "description":"abbr"
            }
        }
        """

    def Snip2VScode_dict(self, path, SnipDict) -> dict:
        with open(path) as f:
            #textList = f.read().splitlines()
            for s_line in f:
                if re.match(self.kwds.include,s_line):
                    # include_function()
                    pass
                elif re.match(self.kwds.comment,s_line):
                    pass
                elif re.match(self.kwds.snippet,s_line):
                    self.reset()
                    self.name = self.get_snippet(s_line)
                    SnipDict[self.name] = self.make_template(self.name)
                elif re.match(self.kwds.options,s_line):
                    # self.get_options(s_line)
                    pass
                elif re.match(self.kwds.abbr,s_line):
                    # get_abbr()
                    SnipDict[self.name]['description'] = self.get_abbr(s_line)
                elif re.match(self.kwds.alias,s_line):
                    SnipDict[self.name]['prefix'] += self.get_alias(s_line)
                elif re.match(self.kwds.delete,s_line):
                    # do_delete ()
                    # delete means over write old snippet
                    pass
                elif re.match(self.kwds.tab,s_line):
                    # snippet sentences
                    try:
                        SnipDict[self.name]['body'].append(self.get_sentence(s_line))
                    except:
                        pass
                elif re.match(self.kwds.empty,s_line):
                    # print("Empty Line")
                    pass

        return SnipDict
    
    def reset(self):
        self.indent=r""

    def get_snippet(self, line):
        exp = re.match(r"^snippet(\t| )+", line)
        return re.sub(r"\n",'',line[exp.end():])

    def get_options(self,line):
        exp = re.match(r"^options(\t| )+", line)
        return re.sub(r"\n",'',line[exp.end():])
    
    def get_abbr(self, line):
        exp = re.match(r"^abbr(\t| )+", line)
        return re.sub(r"\n",'',line[exp.end():])

    def get_alias(self,line):
        exp = re.match(r"^alias(\t| )+", line)
        sp = line[exp.end():].split(',')
        return [re.sub(r"\n",'',j) for j in [re.sub(r'^(\t| )+','',i) for i in sp]]

    def get_sentence(self, line):
        if self.indent == r"":
            span = re.search(r" +",line).span()
            width = span[1] - span[0]
            for i in range(width):
                self.indent+=" "
        exp = re.match(self.indent,line)
        text = re.sub(r"\n",'',line[exp.end():])
        text = re.sub(r":#:",r":",text)
        return re.sub(self.indent,r"\t",text)

    def make_template(self,snipname):
        return {
                "prefix":[snipname],
                "body":[],
                "description":""
                }

