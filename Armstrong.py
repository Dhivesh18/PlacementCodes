n=153
t=n
a=[]
while t!=0:
    a.append(t%10) 
    t//=10
x=len(a)
sum = sum((i**x) for i in a)
print(sum,a)

