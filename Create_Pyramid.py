'''
Problem Statement-:

Identify the logic behind the series

6 28 66 120 190 276….

The numbers in the series should be used to create a Pyramid. The base of the Pyramid will be the widest and will start converging towards the top where there will only be one element. Each successive layer will have one number less than that on the layer below it. The width of the Pyramid is specified by an input parameter N. In other words there will be N numbers on the bottom layer of the pyramid.

The Pyramid construction rules are as follows

First number in the series should be at the top of the Pyramid
Last N number of the series should be on the bottom-most layer of the Pyramid, with Nthnumber being the right-most number of this layer.
Numbers less than 5-digits must be padded with zeroes to maintain the sanctity of a Pyramid when printed. Have a look at the examples below to get a pictorial understanding of what this rule actually means.
Example

If input is 2, output will be

00006
00028 00066
If input is 3, output will be

00006
00028 00066
00120 00190 00276

'''
n=input().split()
ch,s=1,""
for i in range(len(n)):
    l=len(n[i])
    while l!=5:
        s+='0'
        l+=1
    s+=n[i] + " "
lis=[i for i in s.split()]
while lis:
    c,i=0,0
    while ch!=c:
        print(lis[i],end=" ")
        lis.remove(lis[i])
        c+=1
    ch+=1
    print("\r")