n=1
x=[i for i in range(1,n) if n%i == 0]
if len(x) == 1:
    print("Prime number")
else:
    print("Not a prime number")
