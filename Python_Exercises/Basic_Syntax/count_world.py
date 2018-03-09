#!/usr/bin/env python

import os
import sys
import re

if len(sys.argv)<2 or sys.argv[1] in {"-h", "--help"}:
    print('usage:you are supposed to input the path of file')
    exit()

if not os.path.isfile(sys.argv[1]):
    print('error:the path of file is not exist')
    exit()

dict = {}
sum_count = 0
with open(sys.argv[1], 'r') as f:
    for line in f.readlines():
	line = re.sub(r'[^\w\d\-]',' ',line)
        line = re.sub(r"(\\s\-)|\\s+|\t|\r",' ',line)
        line = re.sub(r"-{2,}",' ',line)
        line = re.sub(r"'{2,}",' ',line)
        line = re.sub('\s\-',' ',line)
	 
        for word in line.split():
            if not word in dict:
                dict[word.lower()] = 0
            dict[word.lower()] +=1
            sum_count += 1

li = sorted(dict.items(), key = lambda d:d[1], reverse = True )

print('file is %s' % sys.argv[1]) 
print('total num of worlds is %d' % sum_count)

for li_word in li:
    print('%s count: %d \t' % (li_word[0],li_word[1]))    



