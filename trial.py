# a=[1,2,1,3,3]
# b,c=[],[]
# for i in a:
#     if a.count(i)>1:
#         b.append(i)
# for i in b:
#     ind=a.index(i)
#     c.append(ind)
#     a[ind]='a'
# print(c)

# a,c=[1,2,3,2,1],0
# for i in range(1,len(a)):
#     if (sum(a[0:i]) and sum(a[i+1:]))==a[i]:
#         print(a[i])

# import copy
# a,c=[1,2,3,4,5],0
# for i in range(len(a)):
#     c=copy.deepcopy(a)
#     c.pop(i)
#     print(c)

# s=input().split(",") # Input = Zoom healthcare,17
# print(s)
# # Output = Zoom_+_healthcare
# t=s[0].replace(" ","_+_")
# print(t)

# import math
# for i in [int(input()) for _ in range(int(input()))]:
#     if i==math.pow(int(math.sqrt(i)),2):
#         print(i)

s="101a0sd1000001"   # input   
# s="1000010101"       # input
k=s.split("1")
print(sum(1 if len(i)==i.count("0") and i!="" else 0 for i in k))

import numpy


