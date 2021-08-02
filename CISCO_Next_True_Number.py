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
def true_number(i):             # function
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
    print(c,co)
    if co>c:
        return c
    return co

a=int(input("Enter a number"))            
print(true_number(a))






