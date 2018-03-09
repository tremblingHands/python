#!/usr/bin/env python

def longer_than(*l):
    s = int(l[0])
    result = []
    for str in l[1:]:
        if len(str) > s:
            result.append(str)
    return result


def main():
    print(longer_than(3, 'hit', 'me', 'baby', 'one', 'more', 'time'))


if __name__ == '__main__':
    main()



