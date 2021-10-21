import math

s = "haveaniceday"
s.replace(" ","") 
w = len(s)**0.5
d,_=math.modf(w)
w+=1 if d != 0.0 else 0
w=int(w)
new=""
a=[s[j:j+w] for j in range(0,w**2,w)]
if a == "":
    a.remove("")
for j in range(w):
    for t in range(w):
        try:  
            new+=a[t][j]
        except IndexError:
            pass
    new+=" "
print(new)