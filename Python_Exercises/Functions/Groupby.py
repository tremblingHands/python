#!/usr/bin/env python

def groupby(*L):
    keys = map(L[0], L[1:])
    result = dict()
    for i, key in enumerate(keys):
        if not result.get(key):
            result[key] = []
        result[key].append(L[i+1])
    return result

def main():
    r = groupby(lambda(s): s[0], 'hello', 'hi', 'help', 'bye', 'here')
    print(r)

if __name__ == '__main__':
    main()


