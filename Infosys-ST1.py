'''
Sample Test 1 - RPG game Infosys Online Test
'''
c=0
n=int(input("Enter the No. of monster "))
e=int(input("Enter the Initial Experience "))
p=[int(input("Enter the power of monsters ")) for i in range(n)]
b=[int(input("Enter the bonus of monsters ")) for i in range(n)]
d=[[p[i],b[i]]for i in range(n)]
d.sort()
for i,j in d:
    if e>=i:
        e+=j
        c+=1
print(c)

'''
Sample Test 1 - Unique Birthday Gift Infosys Online Test 
'''
a=int(input("Enter max"))
k=int(input("Length of array"))
if k!=1:    
    b=[[j,i] for j in range(1,a+1) for i in range(1,a+1) if i%j==0] 
else: 
    b=[[i] for i in range(1,a+1)]
print(len(b))
