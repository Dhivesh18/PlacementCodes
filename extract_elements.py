def check(i):
    c = a.count(i)
    if c>=2:
        return i
a = [4,6,4,3,4,5,6,6,4,1,2]
k = 2
b=list(set(map(check,a)))
b.pop(b.index(None))
print(b)