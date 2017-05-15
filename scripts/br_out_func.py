
"""
Desired output
|==============|=======|======== |
| INTn InKbps  | nnnn  | nnnn    |
| INTn OutKbps | nnnn  | nnnn    |
| INTn InKbps  | nnnn  | nnnn    |
| INTn OutKbps | nnnn  | nnnn    |
"""

# Set initial values

# Set up lists for later
A1_inbits = ['INTA1 InKbps']
A1_outbits = ['INTA1 OutKbps']
A2_inbits = ['INTA2 InKbps']
A2_outbits = ['INTA2 OutKbps']
A3_inbits = ['INTA3', 'INTA3 InKbps']
A3_outbits = ['INTA3', 'INTA3 OutKbps']
A4_inbits = ['INTA4', 'INTA4 InKbps']
A4_outbits = ['INTA4', 'INTA4 OutKbps']
A5_inbits = ['INTA5', 'INTA5 InKbps']
A5_outbits = ['INTA5', 'INTA5 OutKbps']
A6_inbits = ['INTA6', 'INTA6 InKbps']
A6_outbits = ['INT7', 'INTA6 OutKbps']
A7_inbits = ['INTA7', 'INTA7 InKbps']
A7_outbits = ['INT7', 'INTA7 OutKbps']
A8_inbits = ['INTA8', 'INTA8 InKbps']
A8_outbits = ['INT8', 'INTA8 OutKbps']
A9_inbits = ['INTA9', 'INTA9 InKbps']
A9_outbits = ['INTA9', 'INTA9 OutKbps']
A10_inbits = ['INTA10', 'INTA10 InKbps']
A10_outbits = ['INTA10', 'INTA10 OutKbps']
A11_inbits = ['INTA11', 'INTA11 InKbps']
A11_outbits = ['INTA11', 'INTA11 OutKbps']
A12_inbits = ['INTA12', 'INTA12 InKbps']
A12_outbits = ['INTA12', 'INTA12 OutKbps']
A13_inbits = ['INTA13', 'INTA13 InKbps']
A13_outbits = ['INTA13', 'INTA13 OutKbps']
A14_inbits = ['INTA14', 'INTA14 InKbps']
A14_outbits = ['INTA14', 'INTA14 OutKbps']
E1_inbits = ['EXT1', 'EXT1 InKbps']
E1_outbits = ['EXT1', 'EXT1 OutKbps']
E2_inbits = ['EXT2', 'EXT2 InKbps']
E2_outbits = ['EXT2', 'EXT2 OutKbps']
E3_inbits = ['EXT3', 'EXT3 InKbps']
E3_outbits = ['EXT3', 'EXT3 OutKbps']
E4_inbits = ['EXT4', 'EXT4 InKbps']
E4_outbits = ['EXT4', 'EXT4 OutKbps']


def interfaceRows(record):
    """
    sets start row for each Interface
    next row will be for InKbps
    next row for OutKbps
    """
    inbitlist = []
    outbitlist = []
    if record[0] == "INTA1":
        inbitlist = A1_inbits
        outbitlist = A1_outbits
    elif record[0] == "INTA2":
        inbitlist = A2_inbits
        outbitlist = A2_outbits
    # elif record[0] == "INTA3":
    #     outbitlist = ""
    #     inbitlist = ""
    # elif record[0] == "INTA4":
    #     outbitlist = ""
    #     inbitlist = ""
    # elif record[0] == "INTA5":
    #     outbitlist = ""
    #     inbitlist = ""
    # elif record[0] == "INTA6":
    #     outbitlist = ""
    #     inbitlist = ""
    # elif record[0] == "INTA7":
    #     outbitlist = ""
    #     inbitlist = ""
    # elif record[0] == "INTA8":
    #     outbitlist = ""
    #     inbitlist = ""

    inbitlist.append(record[1])
    outbitlist.append(record[2])
    return
    # outbitlist, inbitlist


def sendtoxcl(ws, row, col):
    """write results to spreadsheet"""
    for item in A1_inbits:
        ws.write(row, col, item, big_num)
        ws.set_column(row, col, 18)
        col +=1
    return
