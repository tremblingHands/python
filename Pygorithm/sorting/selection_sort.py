#!/usr/bin/env python
def sort(_list):
    for i in range(len(_list)-1, 0, -1):
        max = _list[i]
        pos = i
        for j in range(i):
            if _list[j] > max:
                max = _list[j]
                pos = j
        _list[i], _list[pos] = _list[pos], _list[i]
    return _list



def  main():
    my_list = [12, 4, 2, 14, 3, 7, 5]
    print(sort(my_list))

if __name__ == '__main__':
    main()

