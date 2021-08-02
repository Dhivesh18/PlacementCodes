a = [1, 2, 2, 2, 4, 5, 6, 6, 6, 7]
v=[]
for i in range(len(a)):
    b = a[i:i+3]
    try:
        for j in range(1):
            if (b[j]==b[j+1]==b[j+2]):
                v.append(b[j])
    except IndexError:
        pass
print(v)

