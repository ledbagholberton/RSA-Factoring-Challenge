#!/usr/bin/python3
#import pdb; pdb.set_trace()
with open("tests", 'r', encoding='utf-8') as f:
    a = f.read()
    a_l = a.count("\n")
    print (" lineas es archivo: {:}".format(a_l, end=""))
lineas = 0
b = 0
with open("tests", 'r', encoding='utf-8') as f:
    while lineas < a_l:
        n1 = f.readline()
        n1 = int(n1)
        lineas += 1
        flag = 0
        while flag is not 1:
            for a in range (2, n1//2):
                if n1 % a is 0:
                    flag = 1
                    b = n1 / a
                    print ("{:} = {:} * {:}".format(n1, a, b, end=""))
