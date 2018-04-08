#!/usr/bin/env python

def _bubble_sort(_list):
    l = len(_list)
    for i in range(l):
        for j in range(l-1-i):
            if _list[j+1] < _list[j]:
                _list[j], _list[j+1] = _list[j+1], _list[j]
    return _list

def _improved_sort(_list):
    """
    add a flag if no position changing in  a round , break

    """
    l = len(_list)
    for i in range(l):
        flag = 1
        for j in range(l-1-i):
            if _list[j+1] < _list[j]:
                _list[j], _list[j+1] = _list[j+1], _list[j]
                flag = 0
        if flag:
            break
    return _list






def main():
    my_list = [12, 4, 2, 14, 3, 7, 5]
    print(_bubble_sort(my_list))
    print(_improved_sort(my_list))


if __name__ == '__main__':
    main()




