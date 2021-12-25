class Account:
    def __init__(self,no,name,bal):
        self.a, self.b, self.c = no, name,bal
        
class AccountDemo:
    def __init__(self) -> None:
        pass

    def depositAmnt(self,a,dp):
        a.c = a.c + dp
        return a.c

    def withdrawAmnt(self,a,d):
        return "No Adequate balance" if abs(d-a.c)<1000 else abs(d-a.c)

acno = 120
acname = 'Rajesh'
acntbal = 1500
depamnt = 1200
withamnt = 100
acnt = Account(acno,acname,acntbal)
acntdemoobj = AccountDemo()
print(acntdemoobj.depositAmnt(acnt,depamnt))
print(acntdemoobj.withdrawAmnt(acnt,withamnt))
