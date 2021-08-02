l="qwertyuiop[]asdfghjkl;'zxcvbnm,./"
s="s;;upimrrfod;pbr"
new=""
for i in s:
    ind=l.index(i)
    new+=l[ind-1]
print(new)
