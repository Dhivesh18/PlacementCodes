m,n=8,12
low = min(m, n)
while 1:
    if low % m ==0 and low % n == 0:
        break
    low+=1
print(low)

