'''
During the COVID19 pandemic, the status of beds availability is to be tracked

Create a class City with the below attributes:
a,i = city_id of type Number
b,j = state_name of type String
c,k = city_name of type String
d,l = covidbeds of type Number
e,m = avlblcovbeds of type Number
f,n = ventilbeds of type Number
g,o = avlblventilbeds of type Number


Attribute description:
city_id represents Unique ID for the city
state_name represents the state name
city_name represents the city name

covidbeds represents the total covid beds in the city
avlblcovbeds represents the total available covid beds in the city
ventilbeds represents the total ventilator beds in the city
avlblventilbeds represents the total available ventilator beds in the city


Create the __init__ method which takes all parameters in the above sequence. The method should set the value of attributes to parameter values .

Create another class CovBedsAnalysis with the below attributes:
h = analysis_name of type String
i = city_list of type List having city objects

Create the __init__ method which takes all parameters in the above sequence. The method should set the value of attributes to parameter values 
inside the method.

Create another method inside the class with the name get_StateWiseAvlblBedStats

This method is used to find the state wise available covid beds and available ventilator beds and returns a list of tuples with State name,
total available covid beds and total available ventilator beds for each state, sorted by state name.


Note: A state contains multiple cities. Total number of available beds for a respective category (covid or ventilator beds) in a state is the 
sum of the available beds of all the cities in that state for the respective category(covid or ventilator). Refer testcase output for more clarity.


Create another method with the name get_CiitesWithMoreThanAvgOccupiedbeds, which takes state as argument and returns the dictionary with city 
as the key and tuple of occupied covid beds and occupied ventilator beds as value, where number of covid beds occupied and ventilator beds 
occupied are more than the state average for the respective category of beds .


i.e. the City(cities) in the given state to be recorded/resulted( with the data mentioned), should satisfy the below conditions:

Whose occupied covid beds count is more than the "average of Occupied covid beds of all the cities of the given state" and the respective 
City should also contain the Occupied ventilator beds count more than the "average of occupied ventilator beds of all cities of the given state".

For more clarity , please refer the Sample test case Input and Output in below section

If no city is found with the occupied beds more than state average as mentioned above, then return None and display ‘No city available' 
(Without quotes) in main function.


Please note that the search operations(if any as per the requirement ..) should be case insensitive.

Instructions to write main function:

Instructions to write main section of the code
a. You would require to write the main section completely, hence please follow the below instructions for the same.
b. You would require to write the main program which is inline to the "sample input description section" mentioned below and to read the 
data in the same sequence.
c. Create the respective objects(City and CovBedsAnalysis ) with the given sequence of arguments to fulfill the __init__ method requirement 
defined in the respective classes referring to the below instructions.

i. Create a City object after reading the data related to it and add the object to the list of city objects which will be provided to the 
CovBedsAnalysis object while creation.
This point repeats for the number of city objects(considered in the first line of input data) .

ii. Create CovBedsAnalysis object by passing the CovBedsAnalysis name(you can hard-code any name you want) and List of city objects 
( created as mentioned in above
point# c.i ) as the arguments.
d. Take a string value as input depicting the state which is passed to the get_CiitesWithMoreThanAvgOccupiedbeds
e. Call the method get_StateWiseAvlblBedStats mentioned above from the main section.
f. Display the State,total available covid beds and total available ventilator beds received from the method, with a single space in 
between as shown in sample testcase output,
g. Call the method get_CiitesWithMoreThanAvgOccupiedbeds mentioned above from the main section
h. Display the city name, occupied covid beds and occupied ventilator beds with a single space in between as shown in the sample testcase output.
I. If None is returned by the method get_CiitesWithMoreThanAvgOccupiedbeds, display the message ‘No city available' (excluding the quotes).


You can use/refer the below given sample input and output to verify your solution using ' Test against Custom Input ' option in Hackerrank.


Input format for Custom Testing:

a.The 1st input taken in the main section is the number of city objects to be added to the list of cities.
b.The next set of inputs are the values for the attribtes: city_id,state_name,city_name, covidbeds,avlblcovbeds,ventilbeds,avlblventilbeds 
respectively for each city taken one after other and is repeated for number of objects given in the first line of testcase input
c.The last line of input refers the state name which is passed to the function: get_CiitesWithMoreThanAvgOccupiedbeds


Sample Testcase1:

Input:
5
101
Delhi
Delhi
100000
20000
5000
2000
102
Telangana
Hyderabad
200000
40000
1000
500
103
Telangana
Warangal
100000
30000
2000
1000
104
AndhraPradesh
Vijayawada
800000
300000
30000
2500
105
AndhraPradesh
Vizag
500000
100000
6000
1000
AndhraPradesh


Output:

AndhraPradesh 400000 3500
Delhi 20000 2000
Telangana 70000 1500
Vijayawada 500000 27500



Sample TestCase2:

Input:

6
101
Delhi
Delhi
100000
20000
8000
3000
102
Telangana
Hyderabad
200000
100000
12000
6000
103
Telangana
Warangal
100000
50000
1000
500
104
AndhraPradesh
Vijayawada
800000
=>400000
7500
3750
105
AndhraPradesh
Vizag
500000
=>100000
11000
8500
106
Maharashtra
Mumbai
1000000
0
12500
0
maharashtra


Output:

AndhraPradesh 500000 12250
Delhi 20000 3000
Maharashtra 0 0
Telangana 150000 6500
No city available
'''

# class city():
#     def __init__(self,i,j,k,l,m,n,o):
#         self.a = i
#         self.b = j
#         self.c = k
#         self.d = l
#         self.e = m
#         self.f = n
#         self.g = o

# class CovBedsAnalysis():
#     def __init__(self,a,b):
#         self.h = a
#         self.i = b

#     def get_StateWiseAvlblBedStats(self):
#         a=[]
#         l = {i.b: 0 for i in self.i}
#         m = {i.b: 0 for i in self.i}
#         for i in self.i:
#             l[i.b]+=i.e
#             m[i.b]+=i.g
#             j=0
#         for i in self.i:    
#             try:
#                 if not a:   
#                     a.append([i.b,l[i.b],m[i.b]])
#                 else:
#                     c=0
#                     for k in a:
#                         if k[0]==i.b:
#                             c+=1
#                     if c!=1:        
#                         a.append([i.b,l[i.b],m[i.b]])
#                 j+=1
#             except IndexError:
#                 pass
#         a.sort()    
#         return a

#     def get_CiitesWithMoreThanAvgOccupiedbeds(self,s):
#         t,cb,vb,a1,a2=0,0,0,0,0
#         for i in self.i:
#             if s==i.b:
#                 t+=1
#                 cb+=i.d-i.e
#                 vb+=i.f-i.g
#         if t>0:
#             a1=cb/t
#             a2=vb/t
#         print(a1,a2)
#         k=[]
#         for i in self.i:
#             if i.b==s:
#                 c=i.d-i.e
#                 v=i.f-i.g
#                 print(c,v)
#                 if a1<c and a2<v:
#                     k.append([i.c,c,v])
#         return k

# count=int(input())
# l=[]
# for _ in range(count):
#     c=int(input())
#     s=input()
#     cn=input()
#     av=input()
#     v=int(input())
#     avlb=int(input())
#     d=int(input())
#     # c=101
#     # s="Delhi"
#     # cn="Delhi"
#     # av=100000
#     # v=20000
#     # avlb=8000
#     # d=3000
#     # l.append(city(c,s,cn,av,v,avlb,d))
#     # c=102
#     # s="Telangana"
#     # cn="Hyderabad"
#     # av=200000
#     # v=100000
#     # avlb=12000
#     # d=6000
#     # l.append(city(c,s,cn,av,v,avlb,d))
#     # c=103
#     # s="Telangana"
#     # cn="Warangal"
#     # av=100000
#     # v=50000
#     # avlb=1000
#     # d=500
#     # l.append(city(c,s,cn,av,v,avlb,d))
#     # c=104
#     # s="AndhraPradesh"
#     # cn="Vizag"
#     # av=500000
#     # v=100000
#     # avlb=6000
#     # d=1000
#     # l.append(city(c,s,cn,av,v,avlb,d))
#     # c=105
#     # s="AndhraPradesh"
#     # cn="Vijayawada"
#     # av=800000
#     # v=300000
#     # avlb=30000
#     # d=2500
#     # l.append(city(c,s,cn,av,v,avlb,d))    
#     # c=106
#     # s="Maharashtra"
#     # cn="Mumbai"
#     # av=1000000
#     # v=0
#     # avlb=12500
#     # d=0
#     l.append(city(c,s,cn,av,v,avlb,d))
    
# c=CovBedsAnalysis("covid",l)
# state="AndhraPradesh"
# r=c.get_StateWiseAvlblBedStats()
# for i in range(len(r)):
#     for j in range(len(r[i])):
#         print(r[i][j],end=" ")
#     print(" ")
# re=c.get_CiitesWithMoreThanAvgOccupiedbeds(state)
# if len(re)>0:
#     for i in range(len(re)):
#         for j in range(len(re[i])):
#             print(re[i][j],end=" ")
#     print("")
# else:
#     print("No city available") 

class city():
    def __init__(self,i,j,k,l,m,n,o):
        self.a = i
        self.b = j
        self.c = k
        self.d = l
        self.e = m
        self.f = n
        self.g = o

class CovBedsAnalysis():
    def __init__(self,a,b):
        self.h = a
        self.i = b

    def get_StateWiseAvlblBedStats(self):
        a=[]
        l = {i.b: 0 for i in self.i}
        m = {i.b: 0 for i in self.i}
        for i in self.i:
            l[i.b]+=i.e
            m[i.b]+=i.g
            j=0
        for i in self.i:    
            try:
                if not a:   
                    a.append([i.b,l[i.b],m[i.b]])
                else:
                    c=0
                    for k in a:
                        if k[0]==i.b:
                            c+=1
                    if c!=1:        
                        a.append([i.b,l[i.b],m[i.b]])
                j+=1
            except IndexError:
                pass
        a.sort()    
        return a

    def get_CiitesWithMoreThanAvgOccupiedbeds(self,s):
        t,cb,vb,a1,a2=0,0,0,0,0
        for i in self.i:
            if s==i.b:
                t+=1
                cb+=i.d-i.e
                vb+=i.f-i.g
        if t>0:
            a1=cb/t
            a2=vb/t
        k=[]
        for i in self.i:
            if i.b==s:
                c=i.d-i.e
                v=i.f-i.g
                print(c,v)
                if a1<c and a2<v:
                    k.append([i.c,c,v])
        return k

co=int(input())
l=[]
for i in range(co):
    city_id=int(input())
    state_name = input()
    city_name = input()
    covidbeds = int(input())
    avlblcovbeds = int(input())
    ventilbeds = int(input())
    avlblventilbeds = int(input())
    l.append(city(city_id,state_name,city_name,covidbeds,avlblcovbeds,ventilbeds,avlblventilbeds))
    
c=CovBedsAnalysis("covid",l)
state=input()
r=c.get_StateWiseAvlblBedStats()
for i in range(len(r)):
    for j in range(len(r[i])):
        print(r[i][j],end=" ")
    print(" ")
re=c.get_CiitesWithMoreThanAvgOccupiedbeds(state)
if len(re)>0:
    for i in range(len(re)):
        for j in range(len(re[i])):
            print(re[i][j],end=" ")
    print("")
else:
  print("No city available")
            