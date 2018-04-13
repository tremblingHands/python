#!/usr/bin/env python                                                                                                                          

def sort(_list):
    for i in range(1, len(_list)):
        now = _list[i]
        for j in range(i-1, -1, -1):
            if now < _list[j]:
                _list[j], _list[j+1] = _list[j+1], _list[j]
            else:
                break
    return _list




def  main():
    my_list = [12, 4, 2, 14, 3, 7, 5]
    print(sort(my_list))

if __name__ == '__main__':
    main()

