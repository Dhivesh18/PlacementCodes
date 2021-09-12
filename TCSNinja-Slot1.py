# Question 1 PrepInsta
v,w=200,540
y=(w//2)-v
print("TW=",end="")
print(v-y,"FW=",end="")
print(y)

# Question 2 PrepInsta, FacePrep
s='###***'
x,y=s.count("*"),s.count("#")
print(x-y if x>=y else x-y)

# Question 3 FacePrep
x,s=10,""
if x<=100:
    for i in bin(x).replace("0b",""):
        s+= "0" if i=="1" else "1"  
    print(int(s,2))
else:
    print("Wrong input")

# Question 4 FacePrep
n=2
a=[int(input()) for _ in range(n)]
if n>=3:
    b=[a.count(i) for i in a]
    for i in b[::-1]:
        a[b.index(i)]+=1 if n != len(set(a)) and i > 1 else 0 
    print(sum(a))
else:
    print("Wrong input")
    