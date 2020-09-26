#!/usr/bin/env python #use first installed version of python

from base64 import *

flag = open("encodedflag.txt", "r")
result = flag.read()

for i in range(0,5):
        result = b64decode(result)

for i in range(0,5):
        result = b32decode(result)

for i in range(0,5):
        result = b16decode(result)


flag.close()
print(result)

