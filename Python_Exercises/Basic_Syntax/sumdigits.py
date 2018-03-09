#!/usr/bin/env python

import os
from argparse import ArgumentParser

def build_parser():
    parser = ArgumentParser()
    parser.add_argument('--path',
        dest = 'path', help = 'input file_path',
        metavar = 'PATH', required = True)

    return parser
 
def main():
    parser = build_parser()
    options = parser.parse_args()
    if not os.path.isfile(options.path):
        parser.error("file %s doesn't exit" %(options.path))
    
    with open(options.path, 'r') as f:
        print(f.read())
    


if __name__ == '__main__':
    main()
