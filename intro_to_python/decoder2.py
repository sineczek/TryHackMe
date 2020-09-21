
#!/usr/bin/env python3
from base64 import *

f = open("encodedflag.txt","r")
content = f.read()
i = 0
while i < 5:
	content = base64.b16decode(content)
i += 1
i = 0
while i < 5:
	content = base64.b32decode(content)
i += 1
i = 0
while i < 5:
	content = base64.b64decode(content)
i += 1
print(content)
f.close()


