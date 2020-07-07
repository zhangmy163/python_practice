if __name__ == "__main__":
    from M2.module2 import testfun
    print(testfun(2,4))
    
    import M2
    r=M2.module2.testfun(3,5)
    print(r)

    from M2 import *

    r=M2.module2.testfun(3,5)
    print(r)