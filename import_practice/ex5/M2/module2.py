# -*- coding:utf-8 -*-
from os import path,sys
d = path.dirname(__file__)
parent_path = path.dirname(d)
sys.path.append(parent_path)
# print(sys.path)

#在调用M1时，需要M2文件夹有__init__.py文件，
#否则会出现Unable to import 'M1'pylint(import-error)错误
from M1.module1 import caculate

def testfun(n1,n2):
    cacul=caculate()
    r1=cacul.add(n1,n2)
    r2=cacul.sub(n1,n2)
    r=r1*r2
    return r

if __name__ == "__main__":
    print(testfun(2,4))