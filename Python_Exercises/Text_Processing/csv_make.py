#!/usr/bin/env python

import os
import sys
import re
import csv

def main():
#	if len(sys.argv)<2 or not os.path.isfile(sys.argv[1]) :
#	    print("usage: input path of ifconfig_file ")
#	    exit()

        os.system('ifconfig > ifconfig')
        
	fieldnames = ['interface', 'inet', 'status']

	with open('./ifconfig', 'r') as f:
	    with open('ifconfig.csv', 'w') as wf:
                writer = csv.DictWriter(wf, fieldnames=fieldnames)
                writer.writeheader()
		page = re.sub(r'\n\t', ' ', f.read())
                page = re.sub(r':', ' ', page)
                print(page)
		for para in page.split('\n'):
                    if para == '':
                        continue
		    d = {'interface' : '', 'inet' : '', 'status' : ''}
		    npara = para.split()
		    for i, word in enumerate(npara):
			if i == 0:
			    d['interface'] = word
			    continue 
			if word in fieldnames:
                            #print(npara[i+1])
			    d[word] = npara[i+1]
                    print(d)
                    ##writer.writerow(d)
		    writer.writerow(d)

if __name__ == '__main__':
    main()
