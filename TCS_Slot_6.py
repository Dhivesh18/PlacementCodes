'''
Lynda has three children. She wants to distribute N candies among all three in such a way that exactly 
one child gets the maximum number of candies among all three and each child gets at least one candy. 
The task is to find the total number of ways to distribute N candies among the three children. 
Example: 
Input:
6--- Number of candies
Output:
9
Explanation:
There are 9 ways to distribute 6 candies [1,1,4], [1,4,1], [4,1,1], [1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,2,1], and [3,1,2].
[2,2,2], is not valid because three children will be getting the maximum number of candies i.e 2.
'''
import itertools
n=[i for i in range(int(input())-1)]
k,c=int(input()),0
x=list(itertools.product(n,repeat=k))
c = sum(sum(i)==6 and len(set(i))>=len(i)-1 for i in x) 
print(c)

'''
Sum of all numbers in a string
Here the alphanumeric string is : 1xyz23
In the give string , 1+23 = 24
Hence, the output is 24

method 1
'''
import re
n='12abc23'
print(sum(int(i) for i in re.findall('\d+',n)))

'''
method 2
'''
def findSum(s):
    t,S = "0",0
    for j in s:
        if j.isdigit():
            t += j
        else:
            S += int(t); t = "0"
    return S + int(t)
 
print(findSum("12abc23"))
