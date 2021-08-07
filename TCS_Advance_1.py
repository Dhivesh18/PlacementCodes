n=56 #150 = 556, 10 = 25, 17 = Not Possible, 56 = 78 https://youtu.be/Zy9MQZB-fVE
t=n
c=0
a=[]
b=[]
while n!=0:
    n=int(n/10)
    c+=1
if c==1:
    n+=10
    print(n)
elif c==2:
    n=t
    a=[i for i in range(9,0,-1) if n%i==0]
    for i in a:
        for j in a:
            m=i*j
            if m==n:
                k=(i*10)+j
                b.append(k)
    print(b)
    if b:
        print(min(b))
    else:
        print("Not possible")
elif c==3:
    n=t
    a=[i for i in range(9,0,-1) if n%i==0]
    for i in a:
        for j in a:
            m=i*i*j
            if m==n:
                k=(i*100)+(i*10)+j
                b.append(k)
    if b:
        print(min(b))
    else:
        print("Not possible")


