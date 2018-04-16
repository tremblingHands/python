#!/usr/bin/env python
#coding=utf-8
##插值搜索，不同于二分搜索每次选择中间的那一个，插值搜索线性选择

def search(_list, target):
    low = 0
    high = len(_list) - 1
    
    while low <= high:
        pos =low + int(((target - _list[low]) / (_list[high] - _list[low])) * (high - low))
        if _list[pos] == target:
            return pos

        if _list[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

    return -1

def main():
    my_list = [12, 4, 2, 14, 3, 7, 5]

    my_list.sort()

    index = search(my_list, 7)
    print(index)



if __name__ == '__main__':
    main()
