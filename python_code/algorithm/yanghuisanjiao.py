ch1 = ['a', 'b', 'c']
ch2 = ['x', 'y', 'z']

for i in ch1:
    for j in ch2:
        if i == 'a' and j != 'x':
            print(i, j)
        elif i == 'c' and j != 'x' and j != 'z':
            print(i, j)
        elif i == 'b':
            print(i, j)
