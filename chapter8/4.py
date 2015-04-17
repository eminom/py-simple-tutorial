with open('4.py') as f:
    for i, v in enumerate(f.readlines()):
        print('Line {0}:{1}'.format(i,v),end='')