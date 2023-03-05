# 123-456-7890

import time
import os

st = input()

v = True
if len(st) > 12:
    v = False
if st[3] != '-' or st[7] != '-':
    v = False
for i in st:
    if ord(i) >= 48 and ord(i) <= 57 or ord(i) == 45:
        continue
    else:
        v = False

if v == True:
    print("Correct number given")
else:
    print("wrong number given")


start = time.time()

a = 0
for i in range(1000):
    a += (i**100)

end = time.time()

print("The time of execution of above program is :",
      (end-start) * 10**3, "ms")
