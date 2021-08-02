l=1
r=1000
comp=0
for j in range(l,r+1):
    for k in range(l,r+1):
        if j<=k:
            a=bin(j)
            b=bin(k)
            c=a.replace("0b","")
            d=b.replace("0b","")
            p=32-len(c)
            q=32-len(d)
            c=list(c)
            d=list(d)
            for _ in range(p):
                c.insert(0,'0')
            for _ in range(q):
                d.insert(0,'0')
            m=len(c)
            n=len(d)
            s=""
            for i in range(m):
                if c[i]=='1' and d[i]=='0':
                    s+='1'
                elif c[i]=='0' and d[i]=='1':
                    s+='1'
                else:
                    s+='0'
            x=int(s,2)
            # print(j,"+",k,"=",x," and ",c,"+",d,"=",s)
            comp = max(comp, x)
print(comp)
