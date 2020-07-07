if __name__ == "__main__":
    from M2 import *
    # 通过调M2文件夹下的__init__.py中from M2.module2 import *，下方再使用module2.py的方法，则可以不跟文件名
    r=testfun(2,3)
    print(r)