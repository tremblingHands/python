#!/usr/bin/env python
def merge(a, b):
    c = []
    while  len(a) != 0 and len(b) != 0:
        if a[0] < b[0]:
            c.append(a.pop(0))
        else:
            c.append(b.pop(0))
    return c+a+b



def sort(_list):
    if len(_list) <= 1:
        return _list
    mid = len(_list)//2
    return merge(sort(_list[:mid]), sort(_list[mid:]))
    



def main():
    my_list = [12, 4, 2, 14, 3, 7, 5]
    print(sort(my_list))


if __name__ == '__main__':
    main()




