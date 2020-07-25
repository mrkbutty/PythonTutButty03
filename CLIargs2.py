#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# Refactored to provide some structure

import sys

def add(a, b):
    return a+b

def output_calc(a, b, html=False):
    print(f'Answer is {add(a, b)}')

def cli():
    print(f'Argument count {len(sys.argv)}')
    for i, arg in enumerate(sys.argv):
        print(f'Argument {i:>3} : {arg}')

    if len(sys.argv) != 3:
        print('ERROR: Invalid number of arguments', file=sys.stderr)
        return 1

    output_calc(sys.argv[1], sys.argv[2])
    return 0

if __name__=='__main__':
    retcode = cli()
    exit(retcode)

