from base64 import *

f = open("encodedflag.txt", "r")



flag = f.read()

result = ''

#5 times 16
for i in range(0,5):
	result = b64decode(flag)
flag = result;


#5 times 32
for i in range(0,5):
	result = b32decode(flag)
flag = result;


#5 times 64
for i in range(0,5):
	result = b16decode(flag)
flag = result;

print(result);

f.close();


