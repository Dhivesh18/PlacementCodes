import math
import os
import random
import re
import sys

s = "haveaniceday"
s.replace(" ","")
q = len(s)
w = q**0.5
d,m=math.modf(w)
if d != 0.0:
    w+=1
w=int(w)
a=[]
j=0
new=""
for _ in range(w):
    f=j+w
    a.append(s[j:f])
    j+=w
if a == "":
    a.remove("")
for j in range(w):
    for t in range(w):
        try:  
            k=a[t]
            new+=k[j]
        except IndexError:
            pass
    new+=" "
print(new)


