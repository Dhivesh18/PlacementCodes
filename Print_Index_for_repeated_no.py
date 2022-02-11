# Print Index number for repeated number
a=[1,2,1,3,3]
c=[]
b=[i for i in a if a.count(i)>1]
for i in b:
    ind=a.index(i)
    c.append(ind)
    a[ind]='a'
print(c)
