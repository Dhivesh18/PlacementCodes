import copy

arr=[1,2,3]
n=len(arr)
s=copy.deepcopy(arr)
s.sort()
if s==arr:
    print("yes")
a=b=-1
for i in range(n-1):
    if arr[i]>arr[i+1]:
        a=i
        break
for i in range(n-1,0,-1):
    if arr[i]<arr[i-1]:
        b=i
        break  
t=copy.deepcopy(arr)
t[a],t[b]=t[b],t[a]
if t == s:
    print("yes")
    print("swap",a+1,b+1)
t=copy.deepcopy(arr)
t = t[:a] + t[a:b+1][::-1] + t[b+1:]
if t == s:
    print("yes")
    print("reverse",a+1,b+1)
else:
    print("no")

