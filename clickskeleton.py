#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Template for building command line applications
"""
__author__  = "Mark Butterworth"
__version__ = "0.01 (May 2020)"
__license__ = "MIT"

# Ver 0.01 0720  Initial version

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

import sys
import click

DEBUG = 0
VERBOSE = False


###############################################################################


@click.command()
@click.version_option(version=__version__)
@click.help_option()
@click.argument('filename')
@click.argument('actions', nargs=-1)
@click.option('--listpaths', '-l', is_flag=True, 
    help='List available metric pathnames in the FILENAME')
@click.option('--timerange', '-t', type=str, default=None, 
    help='Date & time range to process, e.g. YYYYMMDDHHMM:YYYYMMDDMM or -0400:')
@click.option('--verbose', '-v', is_flag=True)
@click.option('--debug', '-D', count=True)
def cli(**args):
    """
    \b
    Produce charts for data FILENAME using ACTION(s)
    Actions can be a mixture of script names and arguments in the form x=y:
    \b
    Stock scripts;
        - healthcheck (default)
        - port
        - ldev
        - hur
    """
    
    if 'debug' in args:
        global DEBUG
        DEBUG = args['debug']
        print('DEBUG is enabled')
        print('args:', args)
    
    if 'verbose' in args:
        global VERBOSE
        VERBOSE = True
    filename = args['filename']
    actionlist = args['actions'] 
    listpaths = args['listpaths']
    timerange = args['timerange']

if __name__ == '__main__':
    retcode = cli()
    exit(retcode)