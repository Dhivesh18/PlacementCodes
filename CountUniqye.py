def fun(i):    
    t=[]
    temp=0
    while i!=0:
        r=i%10
        i//=10
        t.append(r)
    for i in t:
        temp = t.count(i) if t.count(i)>=temp else temp
    return temp

m,n,c=1,100,0
a=[i for i in range(m,n+1)]
for i in a:
    x=fun(i)
    if x<=1:
        print(i)
        c+=1
print(c)