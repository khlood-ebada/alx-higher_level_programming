#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0

    while i is not x:
        try:
            print(my_list[i], end='')
            count += 1
        except IndexError:
            None

    print()
    return (count)
