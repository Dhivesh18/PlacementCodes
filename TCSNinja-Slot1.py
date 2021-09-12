# Question 1
v,w=200,540
y=(w//2)-v
print("TW=",end="")
print(v-y,"FW=",end="")
print(y)

# Question 2
s='###***'
x,y=s.count("*"),s.count("#")
print(x-y if x>=y else x-y)

# Question 3
x,s=10,""
if x<=100:
    a=bin(x).replace("0b","")
    for i in a:
        s+= "0" if i=="1" else "1"  
    print(int(s,2))
else:
    print("Wrong input")
