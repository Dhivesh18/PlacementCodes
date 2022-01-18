'''
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Input n=2 
1+1=2
2=2
Output 
2

Input n=3 
1+1+1=3
2+1=3
1+2=3
Output 
3
'''
n = int(input())
a=[0,1,2]
for i in range(3,n+1):
    a.append(a[i-2] + a[i-1])
print(a[n])
 