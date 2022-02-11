# sourcery skip: remove-redundant-if
n=int(input("Enter Marks "))
if n>80:
    print("A")
elif n>=60 and n<=80:
    print("B")
elif n>=50 and n<=60:
    print("C")
elif n>=40 and n<=50:
    print("D")
elif n>=25 and n<=45:
    print("E")
elif n<25:
    print("F")