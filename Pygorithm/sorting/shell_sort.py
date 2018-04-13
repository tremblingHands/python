#!/usr/bin/env python

##每一次处理都是一次按增量的插入排序
##控制增量，按序插入



def sort(_list):
    gap = len(_list)//2
    while gap > 0:
        for i in range(gap, len(_list)):
            j = i
            now = _list[j]
            while j >= gap and _list[j - gap] > now:
                 _list[j] = _list[j - gap]
                 j -= gap
            _list[j] = now
        gap //= 2
    return _list
            



def  main():
    my_list = [12, 4, 2, 14, 3, 7, 5]
    print(sort(my_list))

if __name__ == '__main__':
    main()









