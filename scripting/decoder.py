#!/usr/bin/env python #use first installed version of python

from base64 import *

b64 = open("b64.txt", "r")
b64r = b64.read()

for i in range(0,50):
        b64r = b64decode(b64r)

b64.close()
print(b64r)
