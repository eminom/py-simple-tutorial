

class Base:
    def __init__(self):
        print("Base init")

    def print(self):
        #print("Alright")
        # print("A = ", a)
        # print("B = ", b)
        # print("C = ", c)
        pass

class Derived(Base):
    def __init__(self):
        print("Derived init")

if "__main__" == __name__:
    b = Base()
    # b.print(b=200,  a=100)
    b = Derived()
    b.print()