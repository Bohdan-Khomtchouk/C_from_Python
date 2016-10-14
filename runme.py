#!/usr/bin/env python
# Copyright (C) 2016 Bohdan Khomtchouk

'''
1) Compile/link C source code to produce an executable
2) Run the executable directly from Python

Note that you can replace "call" with "run" for Python 3.5+
'''

import ctypes
from subprocess import call

call(["gcc", "helloworld.c", "-o", "my_executable"])
ctypes.cdll.LoadLibrary("./my_executable").main()