#!/usr/bin/env python

infile = open("Learn_export.csv", "r")
outfile = open("Learn_export.classlist", "w")
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
