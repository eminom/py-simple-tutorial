


class MyClass:
    name = 'he;;'
    def __init__(self):
        pass

    print("Class vars init done")

a = MyClass()
print(type(a))
print(MyClass.name)