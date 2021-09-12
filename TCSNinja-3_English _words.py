'''
The program will receive 3 English words input from STDIN
1. These 3 words will be read one at a time, int three seperate line
2. The first word should be changed like all vowels should be replaced by %.
3. The second word should be changed like all consonants should be replaced by #.
4. The third word should be changed like all char shold be converted to upper case.  
5. Then concatenate the three words and print them.
https://youtu.be/7nG79nM15Zc
'''
n=input().split()
c,s,v=0,"","aeiou"
for i in n:
    if c==0:
        s+="".join("%" if j in v else j for j in i)                
    elif c==1:
        s+="".join("#" if j not in v else j for j in i)
    elif c==2:
        s+=i.upper()
    c+=1
print(s)
