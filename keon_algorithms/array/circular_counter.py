#!/usr/bin/env python
"""
There are people sitting in a circular fashion,
print every third member while removing them,
the next counter starts immediately after the member is removed.
Print till all the members are exhausted.
For example:
Input: consider 123456789 members sitting in a circular fashion,
Output: 369485271
"""

def fn(l, skip):
    ind, lenth = 0, len(l)
    result = []
    while lenth > 0:
        ind = ind + skip - 1
        ind %= lenth
        lenth -= 1
        result.append(l.pop(ind))
    return result

def main(): 
    l = [1,2,3,4,5,6,7,8,9]
    skip = 3
    print('list : %s  skip : %s' %(l, skip))
    print('result : %s' %fn(l, skip))

if __name__ == '__main__':
    main()





