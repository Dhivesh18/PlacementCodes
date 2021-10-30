
'''
Given a binary string, count number of substrings that start and end with 1.
Input: 100100101
Output: 6
Substring:
1001
1001
101
100101
1001001
100100101
'''
s ="100100101"
c=s.count("1")
print(c*(c-1)//2)    
