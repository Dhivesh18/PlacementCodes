n=int(input("Enter a number:"))
p=[]
r=[]
m=1
for i in range(1,n):   
    a=[i for i in range(1,m) if m%i==0]
    p.append(m) if len(a)==1 else None
    m+=1
print(p)
for i in p:
    for j in p:
        r.append((i,j)) if j-i==6 else None
print(r)
