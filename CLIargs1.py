#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys  # the sys module contains system specific parameters functions

print(dir(sys))

for i, arg in enumerate(sys.argv):
    print(f'Argument{i}: {arg}')

