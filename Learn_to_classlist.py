#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
© 2018 DAVID LAU ALL RIGHTS RESERVED
'''

import re
import sys

file_name_1 = sys.argv[1]
print file_name_1

extension = re.search(".csv", file_name_1)
file_name_2 = file_name_1[:extension.start()] + ".classlist"

print file_name_2

infile = open(file_name_1, "r")
outfile = open(file_name_2, "w")
# comment out header row
outfile.write("#")

line = infile.readline()
while line != "" :
    line = line.rstrip()
    line = line.strip("#")
    line_split = line.split(",")
    print line_split
    #student ID
    line_out = line_split[0] + ":"
    #UW CAS ID
    line_out = line_out + line_split[1].strip("#") + ":"
    #Name
    line_out = line_out + line_split[2] + ", " + line_split[3] + ":"
    #Section
    line_out = line_out + "1:0:0:0:0:0:0:"
    #Last name
    line_out = line_out + line_split[2] + ":0:0:0:0\n"
    outfile.write(line_out)
    line = infile.readline()

infile.close()
