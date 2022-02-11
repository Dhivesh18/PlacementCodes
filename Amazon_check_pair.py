def chkPair(A, size, x):
    for i in range(size - 1):
        for j in range (i + 1, size):
            if A[i] + A[j] == x:
                print("Pair with a given sum " , x , " is (" , A[i] , ", " , A[j] , ")")
                return True
                # print("Valid pair exists")
    return False
    # print("No valid pair exists for " , x)
   
# Driver code
A=[1, -2, 1, 0, 5]
x = 0
# chkPair(A, len(A), x)
print("Valid pair exists" if chkPair(A, len(A), x) else "No valid pair exists for " , x)
