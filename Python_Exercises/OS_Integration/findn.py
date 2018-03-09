#!/usr/bin/env python

import os
import sys

arg = sys.argv
if len(arg) < 2:
    print("usage : input the extentions of files you want to find with spacing separating")

tag = tuple(arg[1:])
for root, dirs, files in os.walk(os.getcwd()):
    for file in files:
        path = os.path.join(root, file)
        if path.endswith(tag):
            print(path)
    

