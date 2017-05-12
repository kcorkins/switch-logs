#!/usr/bin/env python3
# import glob
# import os
# import sys
import xlsxwriter
import re


# XlsxWriter
workbook = xlsxwriter.Workbook('Thur_test.xlsx', {'strings_to_numbers': True})
worksheet1 = workbook.add_worksheet("Bitrates-column")
# worksheet2 = workbook.add_worksheet("Bitrates-runs")
big_num = workbook.add_format({'num_format': '0'})
worksheet1.set_column('B:C', 18, big_num)


# Write header for Column Worksheet
worksheet1.activate()
worksheet1.write(0, 0, "Port")
worksheet1.write(0, 1, "InKbps", big_num)
worksheet1.write(0, 2, "OutKbps", big_num)

# Write header for runs Worksheet
# worksheet2.activate()
# worksheet2.write(0, 3, "Port")
# worksheet2.write(0, 4, "InKbps")
# worksheet2.write(0, 5, "OutKbps")

row = 1
col = 0
# XlsxWriter


input_file = "Chassis12-05-11-2017_IOModule-1.log"
# uses the filename passed to the program

with open(input_file, "r") as f:
    print f  # prints the name of the file
    for line in f:  # runs through every line in the file

        raw_str = ''.join(line)  # convert list to string

        # Removes ANSI escape characters from string
        ansi_escape = re.compile(r'(\x9B|\x1B\[)[0-?]*[ -\/]*[@-~]')
        str1 = ansi_escape.sub('', raw_str)

        if str1.startswith("Port"):  # if the line starts with "Port"
            colon = str1.find(":")  # Gives the index of the colon
            # PortNum = str1[colon - 6:colon].strip()  # Give me "Port INTXX"
            # Need to adjust for "EXT" ports
            PortNum = str1[colon - 4:colon].strip()  # Give me "Port INTXX"

            # find the first instance of "Kbps" (starts left->right)
            In = str1.find("Kbps")
            # Snag from after the colon to before Kbps
            InBits = str1[colon + 1:In].strip()
            Out = str1.rfind("Kbps")  # start from the right and finds Kbps
            # snag from the end of end of InKbps to the Out (no Kbps)
            OutBits = str1[In + 4:Out].strip()
            # InBits = column[2]
            # OutBits = column[3]
            # print PortNum

            # Copy the values to the cells
            worksheet1.activate()
            # worksheet1.write(row, col, PortNum)
            worksheet1.write(row, col + 1, InBits, big_num)
            worksheet1.write(row, col + 2, OutBits, big_num)
            # print "Row: " + str(row) + " Col: " + str(col)

            row += 1
            """
            This section will place the next run to the right of the previous
            run. Set the value to the highest port number you've captured.
            If you don't want this, either comment the three lines out, or set
            it to a value higher than you've captured (INTA15 for ex.)
            """
            # If we've gone through the captured ports,
            # move a column to the right
            if PortNum == "EXT4":  # Adjust based on number of ports captured
                col += 2  # Move over three colums
                row = 1  # Start from the top
                # formatting crap
                nnum_col = col + 1  # next_number
                nnnum_col = nnum_col + 1  # next_next_number
                worksheet1.set_column(nnum_col, nnnum_col, 18, big_num)
                worksheet1.write(0, nnum_col, "InKbps", big_num)
                worksheet1.write(0, nnnum_col, "OutKbps", big_num)
            # worksheet2.activate()
            # worksheet2.write(row, col, PortNum)
            # worksheet2.write(row, col + 1, (InBits))
            # worksheet2.write(row, col + 2, (OutBits))
            # row += 1


workbook.close()
f.closed
