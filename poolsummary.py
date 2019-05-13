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


def main():
    with open('testdata\poolinfo_150_470282.txt') as fd:
        lines = fd.readlines()

    section = 0
    for i, text in enumerate(lines):
        text = text.strip()

        if text == 'DP' or text == 'TI':
            section = 1
            sectiontype = text

        if text == '':
            section = 0

        if section > 0 and not('No data' in text) and not('No Setting' in text) \
            and not('0[MB]' in text) and not('0[%]' in text):
            print(text)


    return 0
    


if __name__ == '__main__':
    sys.exit(main())
