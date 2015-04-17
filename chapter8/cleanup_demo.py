class Assassin():
    def __init__(self, value):
        self.name = value

    def __enter__(self):
        print("Hello from {0}".format(self.name))

        # exit takes four parameters
    def __exit__(self, a, b, c):
        print("Bye from {0}".format(self.name))


