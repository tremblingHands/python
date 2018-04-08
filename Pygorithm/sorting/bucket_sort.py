#!/usr/bin/env python
import math
from pygorithm.sorting import insertion_sort

bucket_size = 5

def sort(_list):
    min_n = max_n = _list[0]
    for n in _list:
        if n > max_n:
            max_n = n
        if n < min_n:
            min_n = n
    bucket_n = int(math.ceil((max_n - min_n)/bucket_size))+1
    bucket = []
    for i in range(bucket_n):
        bucket.append([])

    for n in _list:
        bucket[int(math.floor((n-min_n)/bucket_size))].append(n)

    result = []
    for n in bucket:
        insertion_sort.sort(n)
        result += n

    return result


def main():
    my_list = [12, 4, 2, 14, 3, 7, 5]
    print(sort(my_list))

if __name__ == '__main__':
    main()



