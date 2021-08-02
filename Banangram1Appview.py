def Check(a):
    for i in range(len(a)):
        if i!=0:
            if i % 2 == 0 and a[i][0] != a[i - 1][len(a[i - 1]) - 1]:
                return "No"
            if i % 2 != 0 and a[i][0] not in a[i - 1]:            
                return "No"
    return "Yes"

arr1 = ['APPLE','LONG', 'GANG', 'GATE'] # NOTE: OUTPUT IS YES
# arr2 = ['APPLE','LONG', 'HEN'] # NOTE: OUTPUT IS NO
print(Check(arr1))