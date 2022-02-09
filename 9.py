# # Task 9
# calculate the frequency of all elements present in a limited range array. You
# are given an unsorted integer array whose elements lie in the range of 0 to
# n-1 where n is array size. Calculate how many times all elements appear in
# the given array/list. Use dictionary for this.

class dictionary:
    def __init__(self):
        self.dic={}
    
    def cal(self,s):
        for i in s:
            c = s.count(i)
            self.dic[i] = c 
            if self.dic[i]>1:
                del self.dic[i]
        print(self.dic)

    
k = dictionary()
a = [20, 2, 20]
k.cal(a)


