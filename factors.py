#!/usr/bin/python3
#import pdb; pdb.set_trace()
import math
import sys

filename = sys.argv[1]

with open(filename, 'r', encoding='utf-8') as f:
    a = f.read()
    a_l = a.count("\n")
lineas = 0
b = 0
with open(filename, 'r', encoding='utf-8') as f:
    while lineas < a_l:
        n1 = int (f.readline())
        lineas += 1
        a = 2
        while a < n1//2:
            if math.fmod(n1, a) == 0:
                print ("{:d} = {:d} * {:d}".format(n1, a, int(n1/a), end=""))
                a = n1
            a += 1
