import math
import os
import random
import re
import sys


''' Task
Given an integer,

, perform the following conditional actions:

    If 

is odd, print Weird
If
is even and in the inclusive range of to
, print Not Weird
If
is even and in the inclusive range of to
, print Weird
If
is even and greater than

    , print Not Weird

Input Format

A single line containing a positive integer,

.

Constraints

Output Format

Print Weird if the number is weird; otherwise, print Not Weird.'''


if __name__ == '__main__':
    n = int(input().strip())
    if(n>1 and n<=100):
        if(n%2!=0):
            print("Weird")
        elif(n>2 and n<6):
            print("Not Weird")
        elif(n>6 and n<21):
            print("Weird")
        elif(n>20):
            print("Not Weird")