#!/usr/bin/env python
#counting sort only for positive integer sorting
def sort(_list):
    max_n = _list[0]
    for n in _list:
        if max_n < n:
            max_n = n

    counting = [0] * (max_n + 1)
    for n in _list:
        counting[n] += 1
    
    ind = 0
    for i in range(max_n + 1):
        for j in range(counting[i]):
            _list[ind] = i
            ind += 1   

    return _list

def main():
    my_list = [12, 4, 2, 14, 3, 7, 5]
    print(sort(my_list))




if __name__ == '__main__':
    main()





