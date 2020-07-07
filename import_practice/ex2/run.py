
if __name__ == "__main__":
    from module1 import caculate
    cacul=caculate()
    r1=cacul.add(3,4)
    print(r1)

    import module1
    cacul=module1.caculate()
    r2=cacul.sub(4,6)
    print(r2)
