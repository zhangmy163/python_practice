
if __name__ == "__main__":
    from module1 import add
    r1=add(3,4)
    print(r1)

    import module1
    r2=module1.add(4,6)
    print(r2)