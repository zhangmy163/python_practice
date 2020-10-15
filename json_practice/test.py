# -*- coding:utf-8 -*-
import json
from pathlib import Path
base_dir=Path(__file__).resolve().parent

def formatstr(s):
    l='\"'+s+'\"'
    return l

def existjson(s,js):
    if (s in js):
        return(formatstr(str(js[s])))
    else:
        return(formatstr("is not exist"))


# message,script,line,error,url,ua,other
with open(str(base_dir)+"/file/error.csv",'a') as wf:
    wf.writelines("message"+","+"script"+","+"line"+","+"error"+","+"url"+","+"other"+","+"ua"+"\n")
with open(str(base_dir)+"/file/error.log",'rb') as f:
    for line in f:
        l=[]
        data=json.loads(line)
        # print(line)
        # print(data["info"])

        try:
            datainfo=json.loads(data["info"])
        except:
            msg=formatstr("info is not json")
            scr='\"\"'
            li='\"\"'
            err='\"\"'
            url='\"\"'
            other=formatstr(data["info"]).replace(",",";")
            with open(str(base_dir)+"/file/error.csv",'a') as wf:
                wf.writelines(msg+","+scr+","+li+","+err+","+url+","+other)
        else:
            msg=existjson("message",datainfo)
            scr=existjson("script",datainfo)
            li=existjson("line",datainfo)
            err=existjson("error",datainfo)
            url=existjson("url",datainfo)
            other='\"\"'
            with open(str(base_dir)+"/file/error.csv",'a') as wf:
                wf.writelines(msg+","+scr+","+li+","+err+","+url+","+other)
        with open(str(base_dir)+"/file/error.csv",'a') as wf:
                wf.writelines(","+formatstr(data["ua"])+"\n")
