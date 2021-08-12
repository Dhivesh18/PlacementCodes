'''
Question 1
'''
import math
r1=int(input())
n=int(input())
r2=int(input())
x=int(input())
total=x/60
r_1=r1*n
r_2=r2*(math.ceil(total) - n)
print(r_1 + r_2)

'''
Question 2
'''
from itertools import permutations

def fun(ch):
    for i in p:
        if i[i.index(ch)] == i[i.index(ch)+1]:
            del p[p.index(i)]
        
inp=[int(i) for i in input().split()]
a=['R' for i in range(inp[0])]
a+=['G' for i in range(inp[1])]
a+=['T' for i in range(inp[2])]
p=list(set(permutations(a)))
if inp[0]>1:
    ch='R'
    fun(ch) 
if inp[1]>1:
    ch='G'
    fun(ch)
if inp[2]>1:
    ch='T'
    fun(ch)
c = sum(1 if i[i.index(ch)] != i[i.index(ch)+1] else 0 for i in p)
print(p,c)
