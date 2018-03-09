#!/usr/bin/env python


def mymul(*L):
    sum = 1
    for num in L :
        try:
            num = float(num)
            sum *= num
        except Exception as e:
            pass 
        finally:
            pass
    return sum

def main():
    print(mymul('foo', 'bar', 10, 20))
    print(mymul())
    print(mymul(7))


if __name__ == '__main__':
    main()

