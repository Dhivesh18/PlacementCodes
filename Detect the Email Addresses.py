import re
N=int(input())
myStr = " ".join(input() for i in range(N))
lst = list(set(re.findall('[\w.]+@[\w.]+\w+', myStr)))
lst.sort()
# for i in range(len(lst)):
#     print(lst[i],end=";") if i<len(lst)-1 else print(lst[i])
print(";".join(lst))


