#!/usr/bin/env python
#coding=utf-8
##返回变位词
from collections import Counter

def is_anagram(word, _list):
    word = word.lower()
    anagrams = []
    for words in _list:
        if word != words.lower():
            if Counter(word) == Counter(words.lower()):
                anagrams.append(words)
    return anagrams

def main():
    word = 'listen'
    list = ['we', 'are', 'silent']
    print(is_anagram(word, list))

if __name__ == '__main__':
    main()
