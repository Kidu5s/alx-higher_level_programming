#!/usr/bin/python3
def uppercase(str):
     for i in range(0, len(str)):
         if ord(str[i]) <= 122 and ord(str[i]) >= 97:
             print("{}".format(str[i] + ' ')
