# Question 1
a=[1,0,2,0,1,0,2]
a.sort()
print(a)

# Question 2
a,b,s=[12,2,2,5],[],0
for _ in range(len(a)-1):
    x,y=a.pop(a.index(min(a))),a.pop(a.index(min(a)))
    s=x+y
    b.append(s),a.append(s)
print(sum(b))
