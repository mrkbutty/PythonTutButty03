#! /usr/bin/env python3
# -*- coding: utf-8 -*-


# Plan:
'''
1) Read poolinfo.txt file and summarize the contents.
Note structure is;
Section headings for each pool type;  DP, DP(Multi-Tier), DP(?????), TI
First pool overview starts with "POOL-ID : 0x????( ?)" (note the seperating ":")
Also pool overview shows unused items values as "0[MB]" or "0[%]" or "No Setting" or "No Data" 
Each pool detail list is seperated by a blank line

2) Output a summary of pool ID, type, sizes into a xlsx file

'''

import sys


def main():
    pass


if __name__ == '__main__':
    sys.exit(main())
