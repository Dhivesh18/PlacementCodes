#!/bin/python3
import math
import os
import random
import re
import sys

def appendAndDelete(s, t, k):
    c=0
    for i,j in zip(s,t):
            if i==j:
                c+=1
                print(i,c)
            else:
                break    
    print(c)
    l=len(s)+len(t)
    print("Total",l)
    if l<= 2*c+k and l%2==k%2 or l<k:
        print(l%2,k%2)
        return 'Yes'
    else:
        return 'No'
        
if __name__ == '__main__':
    s = "hackerhappy"
    t = "hackerrank"
    k = 9
    result = appendAndDelete(s, t, k)
    print(result)
