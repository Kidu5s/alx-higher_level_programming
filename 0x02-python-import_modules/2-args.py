#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    leng = len(argv) - 1
    if len(argv) == 1:
        print("{} arguments.".format(leng))
    elif len(argv) > 1:
        if len(argv) == 2:
            print("{} argument:".format(leng))
            print("{}: {}".format(leng, argv[leng]))
        elif len(argv) > 2:
            print("{} arguments:".format(leng))
            for i in range(0, leng):
                print("{}: {}".format(i + 1, argv[i + 1]))
