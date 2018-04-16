#!/usr/bin/env python
#coding=utf-8
## 先指数确定搜索上限，再用二分查找

from binary_search import search as bs

def search(_list, target):
    low = 1
    while low < len(_list) and _list[low] <= target:
        low *= 2
    
    return bs(_list[low // 2:], target) + low // 2




def main():
    my_list = [12, 4, 2, 14, 3, 7, 5]

    my_list.sort()

    index = search(my_list, 7)
    print(index)



if __name__ == '__main__':
    main()
