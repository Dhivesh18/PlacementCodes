n=int(input("Enter Number"))
s=bin(n)
a=s.replace("0b","")
p=32-len(a)
a=list(a)
for _ in range(p):
    a.insert(0,'0')
print(a)
q = "".join('1' if a[i]=='0' else '0' for i in range(32))
print(q)
print(int(q,2))

