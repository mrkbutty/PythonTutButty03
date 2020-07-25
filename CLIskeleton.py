#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# CLIskeleton.py - Template for building command line applications
# Usage:
#   xxxxxx [options] <arg1> <arg2>

# __author__  = "Mark Butterworth"
# __version__ = "0.01 (May 2020)"
# __license__ = "MIT"

# Copyright 2020 Mark Butterworth
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

# Ver 0.01 0720  Initial version

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

