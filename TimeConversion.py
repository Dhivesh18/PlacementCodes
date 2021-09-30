s="12:40:22AM"
n=int(s[0:2])
if s[8:]=="PM" and s[0:2]!="12":
    print(str(n+12)+s[2:8])
elif s[0:2]=="12" and s[8:]=="AM":
    print("00"+s[2:8])
else:
    print(s[0:8])
    