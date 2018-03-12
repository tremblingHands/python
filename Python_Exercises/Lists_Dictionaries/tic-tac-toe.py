#!/usr/bin/env python

BLANK = ['', '', '']
g = [BLANK] * 3
g[0][0] = 'x'
print('g = %s' % g)



g = [["" for x in range(3)] for x in range(3)]
g[0][0] = 'x'
print('new g = %s' % g)


