numbers="0123456789"
upper_case="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n=int(input())
s=[input() for h in range(n)]
for j in range(n):
    c=0
    k=s[j]
    if len(k)==10:
        for i in range(len(k)):
            if i<=4 and k[i] in upper_case or i>4 and i<10 and k[i] in numbers or i==10 and k[i] in upper_case:
                c+=1
    print("YES") if c==9 else print("NO")
          

