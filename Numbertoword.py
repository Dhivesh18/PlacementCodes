def fun(x):
    return sum(i in l for i in x)
    
l="aeiou"
k = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
    100: "hundred",
}
n=int(input("Enter a number between 1 to 100: "))
if n in k:
    a=fun(k[n])
elif n>=1 and n<=100:
    while n%10!=0:
        r=n%10
        n=(n//10)*10
    if n in k and r in k:
        a=fun(k[n]+k[r])
else:
    print("greater 100")
print(a)