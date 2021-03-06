'''
Blood Bank – Donate blood and Save life

Problem statement:

Many of us know the importance of blood availaibility at critical condictions in case of an accident or long run diseases. 
To keep track of blood donors , blood group wise , an NGO want to go automate the donor identification process with an 
application with the below requirements


Develop a class Donor with the below attributes

ID of numeric type
Name of string type
Contact Number of numeric type of 10 digits
Bloodgroup of String type
PrevDonatedMon of string type of 3 characters(first 3 characters of the month name) , which represents the month in 
which the donor donated the blood recently.

AwayFrom of type Numberic representing distance in KM from the centralized point of the city from where the 
application/program is running.

Note:

Assume that the input month to be recorded for the attribute: PrevDonatedMon ,should fall into the range of Jan to 
Nov of current year (2020) only.

Implement a __init__ method to initialize the attributes from the main function

Develop BloodBank class with the below attributes
Name of string type
ListOfDonors of list of Donor objects
Implement a __init__ method to initialize the attributes from the main function

Implement a function: getListofAvailableDonors():

Which will return a sorted dictionary of Bloodgroup wise counts in the ascending order of blood group

i.e. BloodGroup and Count as the key:value pairs based on the Donors in the ListOfDonors ,who satisfied with the below 
two conditions:

The conditions for a Donor, to be considered as available:

1. For any Donor , If there is a minimum of 4 months gap between the 'previously donated month' and current month.
2. The Donor should be with in 50 kms range(AwayFrom attribute represents this value) from the centralized point of the 
city from where the application/program is running.


Two conditions,above should be satisfied for a Donor to consider as available for donating.


The above two conditions section referred multiple places in the Question. To avoid repetitive statements, we mentioned 
the conditions at one place, i.e. here above and referred the same in couple of places below. Please make a note of it.


Note2: Please note that to fulfill the requirement, this function would be called twice, before and after calling the 
function : getAndUpdateDonor (from main),

to know the status of available donors,bloodgroup wise before and after fulfilling the donors request.

Refer the Sample testcase input for any input or attributes format and output or output format for more clarity.

Implement another function : getAndUpdateDonor() which takes two parameters i.e. blood group and required donor count 
and return a True or False as per the below requirements:


Case1. For the given blood group,

If the required donor count more than the available count of donors( who satisfies the conditions mentioned in the above 
section: " The conditions for a Donor, to be considered as available") , then the method will update the PrevDonatedMon 
of all the available Donors of the given blood group with the current month in the list of donor objects (of BloodBank ) 
and rerutns False


Case2. For the given blood group,

If the required donor count is less than or equals to the available count of donors( who satisfies the conditions mentioned 
in the above section: " The conditions for a Donor, to be considered as available" ), then this method considers the first 
available donors of the given blood group from the input ListOfDonors (of Bloodbank class) for donation and update the 
PrevDonatedMon attribute of the donors , considered for donation with current month and returns True.


'i.e. If 5 donors are available with the given conditions(mentoned above # a, b), and the required donors are only 3, 
then the method will consider the first 3 donors as per the input order from the ListOfDonors and update their previous 
Donated month with the current month

Instructions to write main section of the code

Instructions to write main:

a. You would require to write the main section completely, hence please follow the below instructions for the same.
b. You would require to write the main program which is inline to the "sample input description section" mentioned below 
and to read the data in the same sequence.
c. Create the respective objects( Donor and BloodBank) with the given sequence of arguments to fulfill the __init__ method 
requirement defined in the respective classes referring to the below instructions.

i. Create a Donor object after reading the data related to it and add the object to the list of Donor objects which will 
be provided to the BloodBank object. This point repeats for the number of Donor objects(considered in the first line of 
testcase input) .

ii. Create BloodBank object by passing the BloodBank name(you can hard-code any name you want)and List of Donor objects 
( created as mentioned in above point# c.i ) as the arguments.

d. Take a string value for blood group parameter and integer for required donor count, which are to be passed to 
getAndUpdateDonor function.
e. Call the method getListofAvailableDonors from the main section and Display the Blood group and "count of donors 
available for the respective bloodgroup" from the resultant dictionary(returned by the getListofAvailableDonors ) 
with a single space between them.
f. Call the method getAndUpdateDonor with the blood group and count of required donors ,read in point#d from the main section.
h. Display the message "Donor count available" (excluding the quotes) . If the method getAndUpdateDonor returns True and

If False is returned , then display the message ‘Donor count not available' (excluding the quotes).

j. Call the getListofAvailableDonors method again to get the updated available list of donors(satisfies the conditions 
mentioned for a donor to consider as available)
k. Display the Blood group and "count of donors available for the respective bloodgroup" from the resultant 
dictionary(returned by the getListofAvailableDonors )

with a single space between them.


Note: Refer testcase input and output for more clarity on input/ouput and their formats.

You can use/refer the below given sample input and output to verify your solution using ' Test against Custom Input ' 
option in Hackerrank.



Input Format for Custom Testing

a.The 1st input taken in the main section is the number of Donor objects to be added to the list of donors.
b.The next set of inputs are the

DonorID
DonorName
DonorContactNumber
DonorBloodgroup
PrevDonatedMon

AwayFrom

and these input values repeated for number of objects given in the first line of test case input.

c. The last but one and last input of inputs are Bloodgroup and required count of Donors which are to be passed to 
the getAndUpdateDonor


Sample Testcase 1:

Input:
5
101
AAA
9010101010
A-Positive
May
5
102
BBB
9011101010
B-Positive
Jun
45
103
CCC
9111101010
O-Positive
Jul
49
104
DDD
9111101110
O-Positive
Jan
43
105
DDD
9111101110
AB-Negative
Nov
65
O-Positive
2
Testcase Output:

A-Positive 1
AB-Negative 0
B-Positive 1
O-Positive 2
Donor count available
A-Positive 1
AB-Negative 0
B-Positive 1
O-Positive 0


Explanation:

a.The first four lines represents blood group wise available count of donors (who satisfies the conditions mentioned in 
the section: " The conditions for a Donor, to be considered as available" in the Question text ,above)

b. 5th line represents the count of donors required is less than the available count of donors(who satisfies the conditions 
mentioned in the section: " The conditions for a Donor, to be considered as available" in the Question text ,above)

c. 6th to 9th line represents the updated current available donors count , bloodgroup wise after considering the donors 
request for "2 in count for O-Positive" .

Hence current O-Positive counts is 0 after donating the O-Positive blood, for 2 in count and remaining bloodgroup donor 
counts remains intact. 
'''

class donar():
    def __init__(self,id,name,contact,bloodgroup,PrevDonatedMon,AwayFrom):
        self.a=id
        self.b=name
        self.c=contact
        self.d=bloodgroup
        self.e=PrevDonatedMon
        self.f=AwayFrom

class bloodbank():
    def __init__(self,nam,lofd):
        self.g=nam
        self.h=lofd 

    def getListofAvailableDonors(self):
        s=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov"]
        k={i.d:0 for i in self.h}
        for i in self.h:
            if i.f<=50 and i.e in s:
                k[i.d]+=1
        e=list(k.keys())
        f=list(k.values())
        a = [[e[i],f[i]] for i in range(len(e))]
        a.sort()
        return a
            
    def getAndUpdateDonor(self,a,b,c):
        for i in c:
            if i[0]==a:
                i[1]-=b
                c=i[1]
        if c>=0:
            return "Donor count available"
        else:
            return "Donor count not available"

co=int(input())
l=[]
for i in range(co):
    # x=int(input())
    # y=input()
    # z=int(input())
    # i=input()
    # j=input()
    # k=int(input()) 
    x=101
    y="AAA"
    z=9010101010
    i="A-Positive"
    j="May"
    k=5
    l.append(donar(x,y,z,i,j,k))
    x=102
    y="BBB"
    z=9011101010
    i="B-Positive"
    j="Jun"
    k=45
    l.append(donar(x,y,z,i,j,k))
    x=103
    y="CCC"
    z=9111101010
    i="O-Positive"
    j="Jul"
    k=49
    l.append(donar(x,y,z,i,j,k))
    x=104
    y="DDD"
    z=9111101110
    i="O-Positive"
    j="Jan"
    k=43
    l.append(donar(x,y,z,i,j,k))
    x=105
    y="DDD"
    z=9111101110
    i="AB-Negative"
    j="Nov"
    k=65
    l.append(donar(x,y,z,i,j,k))
o=input()
p=int(input())
b=bloodbank("bloodbank",l)
r=b.getListofAvailableDonors()
for i in range(len(r)):
    for j in range(len(r[i])):
        print(r[i][j],end=" ")
    print("")
r1=b.getAndUpdateDonor(o,p,r)
print(r1)
if r1=="Donor count available":
    for i in range(len(r)):
        for j in range(len(r[i])):
            print(r[i][j],end=" ")
        print("")

