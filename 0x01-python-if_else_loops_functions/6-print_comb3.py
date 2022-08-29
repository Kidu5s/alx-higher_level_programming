#!/usr/bin/python3
for i in range(0, 10):
    for j in range(0, 10):
        if i < j and i + j != 17:
            print("{0}{1},".format(i, j), end=' ')
        elif i < j and i + j == 17:
            print("{0}{1}".format(i, j))
