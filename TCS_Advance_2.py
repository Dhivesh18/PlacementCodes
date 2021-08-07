'''
Football league points
https://youtu.be/9hy0aTlXsJw
'''
chk="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
N=int(input())
a=[input().split() for _ in range(int(N*(N-1)/2))]
s = {} 
for i,j,_ in a:
    if i in chk and j in chk:
        s[i],s[j]=0,0
    else: 
        s[i],s[j]=1,1
if max(s.values())!=1:
    for i,j,k in a:
        if k[0]>k[2]:
            s[i]+= 3 
        elif k[0]<k[2]:
            s[j]+= 3  
        else:
            s[i]+= 1 
            s[j]+= 1 
    m, o = list(s.keys()), list(s.values())
    print(m[o.index(max(s.values()))])
    print(max(s.values()))
else:
    print("Name of the teams is lower case") 