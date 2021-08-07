'''
Question 1
'''
a=[int(input()) for _ in range(int(input()))]    
b=[i for i in a if i%10!=0]
b+=[i for i in a if i%10==0]
print(b)
'''
Question 2
'''
a=[int(input()) for _  in range(int(input()))]
for _ in range(int(input())):
    a.append(a.pop(0))
print(" ".join(str(i) for i in a))
