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
print("\n")

'''
*
* *
* * *
* * * *
* * * * *
* * * * * *
* * * * * * *
'''
s=["*" if i==0 else " " for i in range(n+1)]
for i in range(1,n+1):
    print(" ".join(s))
    s[i]="*"
print("\n")

'''
            *
          * *
        * * *
      * * * *
    * * * * *
  * * * * * *
* * * * * * *
'''
n*=2
s=["*" if n//2==i else " " for i in range(n//2+1)]
s.pop(0)
for _ in range(n//2):    
    print(" ".join(s))
    s[s.index("*")-1]="*"
print("\n")

'''
* * * * * * *
  * * * * * *
    * * * * *
      * * * *
        * * *
          * *
            *
'''

n=7
s=["*" for _ in range(n)]
for i in range(n):    
    print(" ".join(s))
    s[i]=" "
print("\n")

'''
* * * * * * *
* * * * * *
* * * * *
* * * *
* * *
* *
*
'''
s=["*" for _ in range(n)]
for i in range(n):    
    print(" ".join(s))
    s[-i-1]=" "
print("\n")

'''
      *
     * *
    * * *
   * * * *
  * * * * *
 * * * * * *
* * * * * * *
'''
n *= 2 # n=7. So, n = 7*2 = 14
s=["*" if n//2==i else "" for i in range(n//2+1)]
s.pop(0)
for _ in range(n//2):    
    print(" ".join(s))
    s[s.index("*")-1]="*"
print("\n")

'''
* * * * * * *
 * * * * * *
  * * * * *
   * * * *
    * * *
     * *
      *
'''

n=7
s=["*" for _ in range(n)]
for i in range(n):    
    print(" ".join(s))
    s[i]=""
print("\n")

'''
      1
     1 1
    1 1 1
   1 1 1 1
'''
n*=2
s=["1" if n//2==i else "" for i in range(n//2+1)]
s.pop(0)
for _ in range(n//2):    
    print(" ".join(s))
    s[s.index("1")-1]="1"
print("\n")

n=7
'''
   1
  111
 11111
1111111
'''
# Method 1
s=["1" if n//2==i else " " for i in range(n)]
for _ in range(n//2):    
    print("".join(s))
    s.insert(s.index("1"),"1")
    s.insert(s.index("1"),"1")
    s.pop(0)
print("\n")

# Method 2
s=["1" if n//2==i else " " for i in range(n)]
for _ in range(n//2):    
    print("".join(s))
    s[s.index("1")-1]=s[-s.index("1")-1]="1"
print("\n")

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
print("\n")

# Method 2
s=["1" if n//2==i else " " for i in range(n)]
for _ in range(n//2+1):    
    print("".join(s))
    s[s.index("1")-1]=s[-s.index("1")-1]="1"
for i in range(n//2+1):    
    s[i]=s[-i-1]=" "
    print("".join(s))
print("\n")

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
print("\n")

'''
Pascal’s triangle pattern using numbers
1 
1 1 
1 2 1 
1 3 3 1 
1 4 6 4 1 
1 5 10 10 5 1 
1 6 15 20 15 6 1
'''
n=7
b=[[1]]
for _ in range(1,n):
    a=[]
    l=b[-1]
    a.append(1)
    for c in range(len(l)):
        try:
            a.append(l[c]+l[c+1])
        except IndexError:
            a.append(1)
    b.append(a)
for i in b:
    print(" ".join(str(j) for j in i))
print("\n")
