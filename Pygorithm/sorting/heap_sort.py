#!/usr/bin/env python

def downshift(_list, st, en):
    l = r = _list[st]
    if st*2+2 <= en:
        r = _list[st*2+2]
    if st*2+1 <= en:
        l = _list[st*2+1]
    if _list[st] >= l and _list[st] >= r:
        return
    if l >= r:
        _list[st],  _list[st*2+1] =  _list[st*2+1],  _list[st]
        downshift(_list, st*2+1, en)
    else:
        _list[st],  _list[st*2+2] =  _list[st*2+2],  _list[st]
        downshift(_list, st*2+2, en)

def heap(_list):
    st = len(_list)/2
    while st >= 0:
        downshift(_list, st, len(_list)-1)
        st -= 1

def sort(_list):
    heap(_list)
#    print("heap _list = %s" %_list)
    l = len(_list)
    for i in range (l-1):
        _list[0] , _list[l-1] = _list[l-1] , _list[0]
#        print("list[0](%s)<>list[%s](%s)" % (_list[0], l-1, _list[l-1]))
        l -= 1
        downshift(_list, 0, l-1)
#        print('now _list = %s' % _list)
    return _list

def  main():
    my_list = [12, 4, 2, 14, 3, 7, 5]
    print(sort(my_list))


if __name__ == '__main__':
    main()
