#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# Refactored to split out options from arguments

import sys

USAGETEXT = '''
    usage: CLarg3.py [options] <number1> <number2>
        Adds <number1> to <number2>

        Options:
            -s = subtract <number1> from <number2>
'''

def add(a, b):
    return a+b

def subtract(a,b):
    return a-b

def output_calc(a, b, func, html=False):
    print(f'Answer is {func(int(a), int(b))}')

def cli():
    opts = [ x.lower() for x in sys.argv[1:] if x.startswith('-')]
    args = [ x.lower() for x in sys.argv[1:] if not x.startswith('-')]

    print(f'options: {opts}')
    print(f'arguments: {args}')

    if len(args) != 2:
        print('ERROR: Invalid number of arguments', file=sys.stderr)
        raise SystemExit(USAGETEXT)  # this will error up the stack but will not print a stack trace and will return 1
        return -1

    calc = add
    if '-s' in opts:
        calc = subtract
    
    output_calc(*args, calc)
    return 0

if __name__=='__main__':
    retcode = cli()
    exit(retcode)

