



class MyBase:
    def __init__(self):
        self.name = 'eminm'

    def print(self):
        print("This is me ", self.name)

if __name__ == "__main__":
    a = MyBase()
    a.print()
    k = a.print   ## And binding happens
    k()