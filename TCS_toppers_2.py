'''
Write a program to find the smallest integer value 'b' for the given value of 'a'.
If we multiply the digits of 'b', we should get
'''
a=int(input())
if a<=9:
    b=a+10
    print(b)
else:
    b=[i for i in range(2,10) if a%i==0]
    for i in range(len(b)):
        for j in range(len(b)):
            if a==b[i]*b[j] and b[i]<b[j]:
                print(b[i],b[j])
if not b:
    b="Not Possible"
    print(b)
