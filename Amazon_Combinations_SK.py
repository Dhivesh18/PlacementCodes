from itertools import combinations

a=[12,4,6,5,10,13]
mini,maxi=4,10
b=[i for i in a if mini<=i and maxi>=i]
b.sort()
print(b)
com = combinations(b, 3)
print(list(com))
print(len(list(com))+1)
# Print the obtained combinations
# for i in list(com):
#     print(i)