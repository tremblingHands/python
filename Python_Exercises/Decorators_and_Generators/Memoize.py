#!/usr/bin/env python

m = dict()

def memoize(func):
    def wrapper(*args, **kw):
        if not m.get(args[0]):
            m[args[0]] = func(*args, **kw)
        return m[args[0]]

    return wrapper



@memoize
def fib(n):
    print("fib({})".format(n))
    if n <= 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)



def main():
    print(fib(10))

if __name__ == '__main__':
    main()




