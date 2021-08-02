l=[]
r=[]
s=[]
arr=[2,10,3,7,9,4,6,12,8]
le=len(arr)
p=arr[0]
print(p)
for i in range(1,le):
    if arr[i]>p:
        r.append(arr[i])
    elif arr[i]<p:
        l.append(arr[i])
    print(l,r)
li=len(l)
ri=len(r)
for i in range(0,li):
    s.append(l[i])
s.append(p)
for j in range(0,ri):
    s.append(r[j])
print(s)