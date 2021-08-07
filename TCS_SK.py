'''
Question 1
'''
mi=input()
a=[int(input()) for i in range(mi)]
k=int(input())
for _ in range(k):
    a.insert(0,a.pop())
print(a)

'''
Question 2
'''
# 1st method
def fun(i):    
    temp,t=0,[]
    while i!=0:
        r=i%10
        i//=10
        t.append(r)
    for i in t:
        temp = t.count(i) if t.count(i)>=temp else temp
    return temp

m,n,c=101,200,0
a=[i for i in range(m,n+1)]
for i in a:
    c+= 1 if fun(i)<=1 else 0
print(c)

# 2nd method
m,n,c=11,15,0
a=[i for i in range(m,n+1)]
for i in a:
    c+=1 if len(set(str(i)))==len(str(i)) else 0
print(c)
