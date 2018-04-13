#!/usr/bin/env python

def sort(_list):
    if len(_list) <= 1:
        return _list

    pivot = _list[len(_list)//2]
    left = [x for x in _list if x < pivot]
    middle = [x for x in _list if x == pivot]
    right = [x for x in _list if x > pivot]
    return sort(left) + middle + sort(right)



def  main():
    my_list = [12, 4, 2, 14, 3, 7, 5]
    print(sort(my_list))

if __name__ == '__main__':
    main()

