#!/usr/bin/env python3
# import glob
# import os
import sys
import re
import xlsxwriter
from br_functions import *
from br_out_func import *


# file_name1 = sys.argv[1]
# print sys.argv[1]

input_file = "IOM1-20170905_1555.txt"
input_name = input_file.rsplit('.', 1)
out_name = str(input_name[0]) + ".xlsx"
data = []
InBits = ""
OutBits = ""
Port = ""
wb = createWorkbook(out_name)
ws = createWorksheet(wb)
print ws
row = 1
col = 0
big_num = wb.add_format({'num_format': '0'})

with open(input_file, "r") as f:
    print f  # prints the name of the file
    for line in f:  # runs through every line in the file
        str1 = cleanup(line)  # strip out VTY, put line into form we can use
        record = parseBitRateCounters(str1)  # parses the counters for ea. port
        if record != None:  # if we found a line with real data
            # record looks like ['INTA2', '920', '931']
            toExcel(record)
            data.append(record[1])  # adds results to huge data string
            # data looks like [['INTA1', '20', '31'], ['INTA2', '920', '931']]
            portnames = getportlist(record)  # get a list of ports
            interfaceRows(record)
            # howmanyrows = len(portnames)
            # #print howmanyrows
            # getrow = interfaceRows(record)  # defines row for Interface records
            # inbits = intinbits(record)
            # outbits = intoutbits(record)
#data.sort(key=lambda tup: tup[0])


# print A1_inbits
# print A1_outbits
# print A2_inbits
# print A2_outbits
for item in A1_inbits:
    ws.write(row, col, item, big_num)
    ws.set_column(row, col, 18)
    col += 1
row += 1
col = 0
for item in A1_outbits:
    ws.write(row, col, item, big_num)
    ws.set_column(row, col, 18)
    col += 1
row += 1
col = 0
for item in A2_inbits:
    ws.write(row, col, item, big_num)
    ws.set_column(row, col, 18)
    col += 1
row += 1
col = 0

for item in A2_outbits:
    ws.write(row, col, item, big_num)
    ws.set_column(row, col, 18)
    col +=1



#for name in portnames:
    #resultlist = buildstr(name, record)
    #portvalues = addvalues(name, record)
    #print resultlist
    # print portvalues
    #print valuelist


# print record

# for port in portnames:

# for interface, inkbps, outkbps in (data):
    # print interface, inkbps, outkbps
    # ws.write(row, col,     interface)
    # ws.write(row, col + 1, inkbps)
    # ws.write(row, col + 2, outkbps)
    # row += 1
    # col += 2





            #ws.write(getrow, col, record[0])  # Port Name
            #print record[0], getrow, inbits

            #print inbits
            #ws.write(getrow, col, inbits)
            #ws.write(getrow + 1, col + 1, record[1])  # InKbps
            #ws.write(runrow + 2, col + 1, record[2])  # OutKbps
            #col += 1
            #row = 1
        # print row, col
            # ws.write(row, col + 2, record[2])









        # ws1.write(1, 4, InBits)
        # worksheet1.write(row, col + 2, OutBits, big_num)
        #
        # if str1.startswith("Port"):  # if the line starts with "Port"
        #     colon = str1.find(":")  # Gives the index of the colon
        #     # PortNum = str1[colon - 6:colon].strip()  # Give me "Port INTXX"
        #     # Need to adjust for "EXT" ports
        #     PortNum = str1[colon - 4:colon].strip()  # Give me "Port INTXX"
        #     print PortNum
        #
        #     # find the first instance of "Kbps" (starts left->right)
        #     In = str1.find("Kbps")
        #     # Snag from after the colon to before Kbps
        #     InBits = str1[colon + 1:In].strip()
        #     Out = str1.rfind("Kbps")  # start from the right and finds Kbps
        #     # snag from the end of end of InKbps to the Out (no Kbps)
        #     OutBits = str1[In + 4:Out].strip()
        #     # InBits = column[2]
        #     # OutBits = column[3]
        #     # print PortNum
        #
        #     # Copy the values to the cells
        #     worksheet1.activate()
        #     worksheet1.write(row, col, PortNum)
        #     worksheet1.write(row, col + 1, InBits, big_num)
        #     worksheet1.write(row, col + 2, OutBits, big_num)
        #     # print "Row: " + str(row) + " Col: " + str(col)
        #
        #     row += 1
        #     """
        #     This section will place the next run to the right of the previous
        #     run. Set the value to the highest port number you've captured.
        #     If you don't want this, either comment the three lines out, or set
        #     it to a value higher than you've captured (INTA15 for ex.)
        #     """
        #     # If we've gone through the captured ports,
        #     # move a column to the right
        #     if PortNum == "EXT4":  # Adjust based on number of ports captured
        #         col += 2  # Move over three colums
        #         row = 1  # Start from the top
        #         # formatting crap
        #         nnum_col = col + 1  # next_number
        #         nnnum_col = nnum_col + 1  # next_next_number
        #         worksheet1.set_column(nnum_col, nnnum_col, 18, big_num)
        #         worksheet1.write(0, nnum_col, "InKbps", big_num)
        #         worksheet1.write(0, nnnum_col, "OutKbps", big_num)
        #     # worksheet2.activate()
        #     # worksheet2.write(row, col, PortNum)
        #     # worksheet2.write(row, col + 1, (InBits))
        #     # worksheet2.write(row, col + 2, (OutBits))
        #     # row += 1

wb.close()
f.closed
