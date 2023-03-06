# a = int(input("abc: "));
# b = int(input("def: "));
# print(a*b);

# c,d = input().split();
# print(int(c)*int(d));
#Your code goes here
# l = int(input());
# b = int(input());
# print(l*b);

from os import *
from sys import *
from collections import *
from math import *
def swap(a, b):
    # Write your coder here.
    temp = a
    a = b;
    b = temp;
    print(a,end=" ");
    print(b);
    
total = input();
total = int(total);
for i in range(total): 
    a,b = input().split();
    a = int(a);
    b = int(b);
    swap(a,b);























