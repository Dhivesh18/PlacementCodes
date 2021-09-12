'''
0,0,2,1,4,2,6,3,8,4 (Asked 25 times in TCS Ninja)
https://youtu.be/e_1T1d5LH5Y
'''
x,y,n,a=0,0,10,[]
for i in range(n):
    if i%2==0:
        a.append(x)
        x+=2
    else: 
        a.append(y)
        y+=1
print(a)
