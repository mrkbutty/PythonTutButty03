#! /usr/bin/env python3
# -*- coding: utf-8 -*-


# Plan:
'''
1) Read poolinfo.txt file and summarize the contents printing the overview only to the screen.
Note structure is;
Section headings for each pool type;  DP, DP(Multi-Tier), DP(?????), TI are followed by (n x pool) details.
First pool overview starts with "POOL-ID : 0x????( ?)" (note the seperating ":")
Also pool overview shows unused items values as "0[MB]" or "0[%]" or "No Setting" or "No Data" 
Each pool detail list is seperated by a blank line

2) Output a summary of pool ID, type, sizes into a xlsx file

'''

import sys
import re

class AwkRule:
    def __init__(self, **kwargs):
        self.start = kwargs.get('start', None)
        self.end = kwargs.get('end', None)
        self.run = kwargs.get('function', None)
        self.end = kwargs.get('skipstart', False)
        self.end = kwargs.get('skipend', False)


class Awk:

    def __init__(self, filename, rules):

        self.rules=list()
        for i in rules:
            self.rules.append(i)






def main():
    with open('testdata\poolinfo_150_470282.txt') as fd:
        lines = fd.readlines()

    section = 0
    for i, text in enumerate(lines):
        text = text.strip()

        match = re.match('^\s+(DP|TI|DP\(.*\))', text)
        if match:
            pooltype = match.group(1)
            section = 1

        match = re.match('')
        
        if text == '':
            section = 0

        if section == 1:
            match = re.match('^(.*):(.*)', text)
            


    return 0
    


if __name__ == '__main__':
    sys.exit(main())
