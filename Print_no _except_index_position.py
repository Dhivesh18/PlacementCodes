# Print the number except index position 
a,c=[1,2,3,4,5],0
for i in range(len(a)):
    c=a[:]
    c.pop(i)
    print(c)
