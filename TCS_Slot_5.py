'''
Question 1 Slot 1 08/08/21
'''
s,a,i="HeyYouDhivesh","ABCDEFGHIJKLMNOPQRSTUVWXYZ",1
t=s.lower()
l=list(t)
sn=list(s)
while i!=len(sn):
    if sn[i] in a:
        l.insert(i," ") 
        sn.insert(i," ")
        i+=1
    i+=1
print("".join(l))

from itertools import combinations

a=[1,2,3,4]
com = combinations(a, 2)
l=list(com)
l+=a
print(l)
print(len(l))
