#!/usr/bin/python3
def max_integer(my_list=[]):
    max_value = my_list[0]
    if my_list == []:
        return None
    else:
        for i in range(len(my_list)):
            if max_value > my_list[i]:
                continue
            else:
                max_value = my_list[i]
    return max_value
