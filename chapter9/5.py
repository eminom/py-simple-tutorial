

class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass


for c in [B,C,D]:
    try:
        raise c()
    except B:
        print("B")
    except C:
        print("C")
    except D:
        print("D")
    finally:
        pass