import sys

class TestClass:
    def __init__(self, w):
        self.name = "hello, world"
        self.w = w
        self.doInit()
        print("init done")

    def print(self):
        print("This is ", self.name)
        print("And w is ", self.w)
        print("Age is ", self.age)
        print(self.more)

    def doInit(self):
        self.age = 28
        self.more = "More information is needed"

if '__main__' == __name__:
    a = TestClass([2,3,5])
    for i in range(0,5):
        sys.stdout.write('*')
    print()
    a.print()