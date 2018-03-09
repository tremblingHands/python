#!/usr/bin/env python

import os

for root, dirs, files in os.walk(os.getcwd()):
    for file in files:
        fp = os.path.join(root, file)
        print fp
        if fp.endswith('.txt'):
            nfile = file
            npath = os.path.join(root, nfile)
            os.rename(fp, npath)
            print(npath)
