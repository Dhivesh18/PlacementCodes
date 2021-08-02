n=10
mid=mi=n//2
s=["*" for i in range(n)]
print("".join(s))
for _ in range(n):
    try:
        s[mid-1]="b"
        s[mi]="b"
        if s.count("b")!=10:    
            print("".join(s))
        mid-=1
        mi+=1
    except IndexError:
        pass
mid=mi=n//2
for i in range(n//2):
    try:
        s[i]="*"
        s[-i-1]="*"
        if s.count("b")==8:
            pass
        elif s.count("b")!=10:    
            print("".join(s))
    except IndexError:
        pass
