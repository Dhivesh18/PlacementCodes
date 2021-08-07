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

# mi=int(input())
# ma=int(input())
# a=[i for i in range(mi,ma+1)]
# c=0
# for i in a:
#     if i not in [1,2,3,4,5,6,7,8,9,10]:
#         t=i
#         s=[]
#         while i!=0:
#             r=i%10
#             i=i//10
#             s.append(r)
#         if len(s)==1:
#             print(t,c)
#             c+=1
# print(len(a)-c)