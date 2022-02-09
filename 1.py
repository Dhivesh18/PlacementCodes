# Task 1
# Implement a list ADT with following interfaces
# a) add_elements(data) – This function adds the argument data into the list.
# b) delete_elements()- This function deletes the last added element in the list. 
#    Also, this will print what data was deleted.
# c) Count_list() – This functions returns the total number of elements in
#    the list.
# d) Sum_list() -This function returns the sum of all data in the list.
# e) Is_empty()-This function returns true or false depending on whether
#    the list is empty or not

class List:
    def __init__(self):                         
        self.items = []
    
    def add_elements(self, data):               # Inserting Elements to List
        self.items.append(data)
    
    def Count_list(self):                       # Count No. of Elements in a List
        return len(self.items)
    
    def Sum_list(self):                         # Sum of the List 
        return sum(self.items)
    
    def Is_empty(self):                         # List is not Empty, it prints true, else false.
        return bool(self.items)

    def delete_elements(self):                  # Delete Element from list
        a = self.items.pop()
        return a

ad = List()
n = [1,2,3]
for i in n:
    ad.add_elements(i)
print("No of Elements ",ad.Count_list())    
print("Sum ",ad.Sum_list())   
print(ad.Is_empty())                                    
print(ad.delete_elements(),"is deleted from List.")   
print(ad.delete_elements(),"is deleted from List.")
print(ad.Is_empty())