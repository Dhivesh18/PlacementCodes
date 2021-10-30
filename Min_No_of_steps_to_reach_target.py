'''
Given an Array of String containing names of Tools (can have duplicates), 
the Starting index and A Target Tool, find the Minimum Number of Steps required 
to reach the target tool from the starting index. The Array is Circular, 
that is, If you reach the End of the array, you can go to its start and vice versa.
'''
a=['saw', 'hammer', 'mallet','file', 'saw', 'ladder', 'scissor']
n,r,l=6,0,0
i=n
s='hammer'
while a[i]!=s:
    i+=1
    i=0 if i>len(a)-1 else i
    r+=1
i=n
while a[i]!=s:
    i-=1
    i=i if i>=0 else len(a)-1
    l+=1
print(min(l, r))
