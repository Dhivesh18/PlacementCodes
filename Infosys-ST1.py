'''
Sample Test 1 - RPG game Infosys Online Test
'''
c,n,e=0,int(input("Enter the No. of monster ")),int(input("Enter the Initial Experience "))
p=[int(input("Enter the power of monsters ")) for _ in range(n)]
b=[int(input("Enter the bonus of monsters ")) for _ in range(n)]
d=[(p[i],b[i]) for i in range(n)]
d.sort()
for i,j in d:
    if e>=i:
        e+=j
        c+=1
print(c)

'''
Sample Test 1 - Unique Birthday Gift Infosys Online Test 
'''
import itertools
n=int(input("Enter max"))
k=int(input("Length of array"))
p,l=[p for p in itertools.product([i+1 for i in range(n)], repeat=k)],0 # this allows repetition
for i in p: 
    c=0
    for j in range(k):
        try:
            if i[j+1]%i[j]==0:                
                c+=1            
        except IndexError:
            pass
    l+=1 if c==k-1 else 0
print(l)
