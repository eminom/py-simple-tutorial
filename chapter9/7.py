

def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]


from sys import stdout
w = stdout.write
for char in reverse('golf'):
    w(char)
print()