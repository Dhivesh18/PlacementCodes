n = (int(input("Number of classes attended "))/int(input("Number of classes held ")))*100
print("Percentage of class attended ",n)
print("Yes, This student is allowed to sit in exam" if n>=75 else "No, This student is allowed to sit in exam") 
