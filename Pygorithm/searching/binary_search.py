#!/usr/bin/env python

def search(_list, target):
    l = 0
    r = len(_list) - 1
    while l <=  r:
        mid = (l + r) // 2
        mid_n = _list[mid]
        if mid_n > target:
            r = mid - 1
        elif mid_n < target:
            l = mid + 1
        else:
            return mid
    return -1


def main():
    my_list = [12, 4, 2, 14, 3, 7, 5]

    my_list.sort()

    index = search(my_list, 7)
    print(index)



if __name__ == '__main__':
    main()
