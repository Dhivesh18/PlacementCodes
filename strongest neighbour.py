a = [1,2,2,3,1,4,5]
b=[]
for i in range(0,len(a)):
    try:
        if a[i]<=a[i+1]:
            b.append(a[i+1])
    except IndexError:
        pass
print(b)