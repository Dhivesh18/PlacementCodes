def fun(i):    
    t=[]
    maxi,temp=0,0
    while i!=0:
        r=i%10
        i//=10
        t.append(r)
    for i in t:
        maxi=t.count(i)
        if maxi>=temp:
            temp=maxi
    return temp

m,n,c=100,125,0
a=[i for i in range(m,n+1)]
for i in a:
    x=fun(i)
    if x<=1:
        print(i)
        c+=1
print(c)