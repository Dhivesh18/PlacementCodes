# Prints the pair with sum closest to x 
def printClosest(arr, n, x):
    res_l, res_r = 0, 0
    l, r, diff = 0, n-1, 10000000
    while r > l:
        if abs(arr[l] + arr[r] - x) < diff:
            res_l,res_r = l,r
            diff = abs(arr[l] + arr[r] - x)
        if arr[l] + arr[r] > x:
            r -= 1
        else:
            l += 1
    print('The closest pair is',arr[res_l],'and',arr[res_r])

# Driver code to test above
if __name__ == "__main__":
    # arr = [0,-1,2,-3,1]
    arr=[1, -2, 1, 0, 5]
    n = len(arr)
    x=0
    printClosest(arr, n, x)
