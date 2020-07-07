# -*- coding:utf-8 -*-
class caculate:
    def add(self,n1,n2):
        self.r=n1+n2
        return self.r
    def sub(self,n1,n2):
        self.r=n1-n2
        return self.r

if __name__ == "__main__":
    cacul=caculate()
    r1=cacul.add(1,2)
    r2=cacul.sub(1,2)
    print(r1)
    print(r2)