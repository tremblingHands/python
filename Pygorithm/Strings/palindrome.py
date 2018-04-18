#!/usr/bin/env python

def is_palindrome(string):
    return string == string[::-1]

def main():
    s = 'omninmo'
    print(is_palindrome(s))

if __name__ == '__main__':
    main()
