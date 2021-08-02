m,n=0,1
k,c=7,0
print(m)
print(n)
while c!=k-2:
    t=m+n
    m=n
    n=t
    c+=1
    print(t)
