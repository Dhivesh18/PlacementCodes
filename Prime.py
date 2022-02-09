#Check Whether NUmber is prime or not
n=149
x=[i for i in range(1,n) if n%i == 0]
if len(x) == 1:
    print("Prime number")
else:
    print("Not a prime number")

# # Prime Number series generator
# n=10
# k=[j for j in range(1,n+1) if len([i for i in range(1,j) if j%i == 0]) == 1]
# print(k)
