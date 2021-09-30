'''
CISCO placement Coding Question - Find Next True Number
Input - 2010
Ouput - 2 
Explanation 
2010 - 1 is not even. So, it is Not True Number.
2009 - 9 is not even. So, it is Not True number 
2008 - All numbers are even. So, it is True number. 
If we decrement the number, the output displayed is 2.
If we increment the number, the output displayed is 10. 
'''
# Method 1
def true_number_method_1(n):
    t=q=0
    o=m=n
    while t==0:
        for i in [int(i) for i in str(n)]:
            if i%2!=0:
                n-=1
                t=0
                break
            t=1
    while q==0:
        for i in [int(i) for i in str(m)]:
            if i%2!=0:
                m+=1
                q=0
                break
            q=1
    return min(o-n, m-o)

# Method 2
def true_number_method_2(i):             # function
    cop=i                       # temp variable for decrementing a number
    c,co=0,0
    while True:
        chk=l=0
        t=i
        while t!=0:             # Getting last digit number of decrement number
            r=t%10
            t=t//10
            l+=1
            if r%2==0:
                chk+=1
        if chk==l:              # all numbers are even chk and count of the number(l) will be same
            break
        c+=1                    # counting the nearest true number (counting decrement)
        i-=1                    # if all numbers are not even chk and count of the number will not be same. So, decrement i 2009 to 2008
    while True:
        chk=l=0
        t=cop                   # temp variable for incremnting a number 
        while t!=0:             # Getting Last digit number of increment number
            r=t%10
            l+=1
            t=t//10
            if r%2==0:
                chk+=1
        if chk==l:             # all numbers are even ch and count of the number(lk) will be same
            break
        co+=1                  # counting the nearest true number (counting increment)
        cop+=1                 # if all numbers are not even chk and count of the number will not be same. So, decrement i 2009 to 2010
    return min(c,co)

a=int(input("Enter a number"))            
print(true_number_method_1(a))
print(true_number_method_2(a))






