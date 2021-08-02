n="aba"
l=list(n)
a=[]
for i in l:
    for j in l:
        for k in l:
            a.append(i+j+k) 
print(set(a))