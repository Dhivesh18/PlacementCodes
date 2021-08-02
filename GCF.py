m,n=12,8
k=max(m,n)
while True:
    if m%k==0 and n%k==0:
        break
    k-=1
print(k)