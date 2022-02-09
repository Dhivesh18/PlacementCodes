'''
Sample Test 2 - Bitwise subsequence 
'''

def lis(a):
    n=len(a)
    # Creating the sorted list
    b=sorted(list(set(a)))
    m=len(b)
     
     
    # Creating dp table for storing the answers of sub problems
    dp=[[-1 for i in range(m+1)] for j in range(n+1)]
     
    # Finding Longest common Subsequence of the two arrays
    for i in range(n+1):
             
        for j in range(m+1):
            if i==0 or j==0:
                dp[i][j]=0
            elif a[i-1]==b[j-1]:
                dp[i][j]=1+dp[i-1][j-1]
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    return dp[-1][-1]
     
# Driver program to test above function
arr = [10, 22, 9, 33, 21, 50, 41, 60]
print("Length of lis is ", lis(arr))
# b=[]
# for i in range(n):
#     try:
#         if (a[i] and a[i+1])*2 > (a[i] or a[i+1]):
#             b.clear()
#             b.append(a[i])
#             b.append(a[i+1])
#     except IndexError:
#         pass
# print(b,len(b))

'''
Sample Test 2 - Grid Path
'''
# n=int(input())
# a=[[int(input()),int(input())]for j in range(2) for i in range(n//2)]

