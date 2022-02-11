n = int(input("Enter length of the list "))
e = sum(i%2==0 for i in [int(input("Enter the values ")) for _ in range(n)])
print("Even Count ",e,", Odd Count",n-e)