n=7
'''
*
**
***
****
*****
******
*******
'''
for i in range(1,n+1):
    print("*"*i)

'''
   1
  111
 11111
1111111
'''
# Method 1
s=["1" if n//2==i else " " for i in range(n)]
for _ in range(n//2+1):    
    print("".join(s))
    s.insert(s.index("1"),"1")
    s.insert(s.index("1"),"1")
    s.pop(0)

# Method 2
s=["1" if n//2==i else " " for i in range(n)]
for _ in range(n//2+1):    
    print("".join(s))
    s[s.index("1")-1]=s[-s.index("1")-1]="1"
'''
   1
  111
 11111
1111111
 11111
  111
   1
'''
# Method 1
s=["1" if n//2==i else " " for i in range(n)]
for _ in range(n//2+1):    
    print("".join(s))
    s.insert(s.index("1"),"1")
    s.insert(s.index("1"),"1")
    s.pop()
    s.pop(0)
for _ in range(n//2+1):    
    s.insert(s.index("1")," ")
    s.pop()
    s.pop()
    print("".join(s))

# Method 2
s=["1" if n//2==i else " " for i in range(n)]
for _ in range(n//2+1):    
    print("".join(s))
    s[s.index("1")-1]=s[-s.index("1")-1]="1"
for i in range(n//2+1):    
    s[i]=s[-i-1]=" "
    print("".join(s))
'''
***1***
**111**
*11111*
1111111
*11111*
**111**
***1***
'''
s=["1" if n//2==i else "*" for i in range(n)]
for _ in range(n//2+1):    
    print("".join(s))
    s[s.index("1")-1]=s[-s.index("1")-1]="1"
for i in range(n//2):    
    s[i]=s[-i-1]="*"
    print("".join(s))
    