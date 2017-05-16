#!/usr/bin/env python3
# import glob
# import os
import sys
import re
import xlsxwriter
from br_functions import *


# input_file = "IOM1-20170905_1555.txt"  # Manual override
input_file = sys.argv[1]  # argv[1] is the name of the file to be parse
input_name = input_file.rsplit('.', 1)  # remove the file name extension
out_name = str(input_name[0]) + ".xlsx"  # add the Excel extension
data = []
valuelist = []
InBits = ""
OutBits = ""
Port = ""
wb = createWorkbook(out_name)
ws = createWorksheet(wb)
print ws
row = 1
col = 0
# big_num = wb.add_format({'num_format': '0'})

with open(input_file, "r") as f:
    print f  # prints the name of the file
    for line in f:  # runs through every line in the file
        str1 = cleanup(line)  # strip out VTY, put line into form we can use
        record = parseBitRateCounters(str1)  # parses the counters for ea. port
        if record != None:  # if we found a line with real data
            # record looks like ['INTA2', '920', '931']
            data.append(record)  # adds results to huge data string
            # data looks like [['INTA1', '20', '31'], ['INTA2', '920', '931']]
            portnames = getportlist(record)  # get a list of ports

# Now the records are in a huge string of strings called 'data'

data.sort(key=lambda tup: tup[0])  # sorts 'data' by portname.
for port in portnames:
    valuelist = getresults(port)  # Doesn't do anything, just a call point
    invalues(port, data)  # retrieves the InKbps values for the port
    toExcel(ws, valuelist, row, col)  # copies the valuelist to wb
    del valuelist[:]  # clears list
    row += 1  # next row
    outvalues(port, data)  # retrieves the OutKbps values for the port
    toExcel(ws, valuelist, row, col)  #copies the valuelist to wb
    del valuelist[:]  # clears list
    row += 1
print portnames  # Just a list of the ports we've gathered

wb.close()
f.closed

if __name__ == "__main__":
    input_file = sys.argv[1]
    # First argument from command line. Name of the file to be parsed
