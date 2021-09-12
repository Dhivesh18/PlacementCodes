'''
1,1,2,3,4,9,8,27,16,81,32,243,64,729,128,2187...
This series is a mixture of 2 series - all the 
odd terms in this series form a geometric series 
and all the even terms form yet another geometric series.
Write a program to find the Nth term in the series. 
https://youtu.be/qEJcAuH7rZg
'''
n=int(input())
a=[1,1,2,3]
if n>=4:
    for i in range(4,n):
        a+=[2*a[i-2] if i%2==0 else 3*a[i-2]]
else:   
    while len(a)!=n:
        a.pop()
print(a)
