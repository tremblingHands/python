#!/usr/bin/env python


def after5(count = []):
    def decorator(func):
        def wrapper(*args, **kw):
            print(count)
            if len(count) == 0:
                count.append(-1)
            count[0] += 1
            if not count[0] < 5:
                return func(*args, **kw)
            else:
                print("call decorator")
                return func(*args, **kw)
        return wrapper
    return decorator

@after5()
def doit():
    print("Yo!")

def main():
    # ignore the first 5 calls
    doit()
    doit()
    doit()
    doit()
    doit()

    # so only print yo once
    doit()    


if __name__ == '__main__':
    main()



