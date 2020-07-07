if __name__ == "__main__":
    import M1
    r=M1.module1.add(0,1)
    print(r)
    
    import M1.module1
    r=M1.module1.add(3,4)
    print(r)

    from M1 import module1
    r=module1.add(2,3)
    print(r)

    from M1.module1 import add
    r=add(1,2)
    print(r)

    