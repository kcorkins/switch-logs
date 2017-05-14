import re
import xlsxwriter

# Print flag
PRINT = 1

# Set up lists for later
A1inbits = ['INTA1', 'INTA1_InKbps']
A1outbits = ['INTA1', 'INTA1_OutKbps']
portlist = []


def cleanup(line):
    raw_str = ''.join(line)  # convert each word in list to strings
    str1 = stripESC(raw_str)
    return str1


def stripESC(raw_str):
    """Strips Escape codes from captured text"""
    ansi_escape = re.compile(r'(\x9B|\x1B\[)[0-?]*[ -\/]*[@-~]')
    str1 = ansi_escape.sub('', raw_str)
    return str1

# def parseBitRateCounters(line, portName):


def parseBitRateCounters(line):
    """
    Takes a line, return parsing of bitrate counters
    INPUT: Line from input file, String
    Output: Array of format; portName, InBits, OutBits
    """
    if line.startswith("Port"):
        portName = re.search(r'INTA\d+|EXT\d+|\d+', line).group()
        record = line.split()  # cuts the line into indiv. strings
        inkbps = record[2]  # gets the InKbsp value (string)
        InBits = inkbps[:-4]  # Removes 'Kbps'
        outkbps = record[3]  # gets the OutKbps value (string)
        OutBits = outkbps[:-4]  # Removes 'Kbps'
        result = [portName, InBits, OutBits]
        return result


def getportlist(record):
    """Get a list of the portnames in use"""
    portname = record[0]
    if portname not in portlist:
        portlist.append(portname)
    return portlist


valuelist = []
item = []
def buildstr(portname, data):
    for name in portname:
        valuelist.append(portname)
        return valuelist


def addvalues(name, data):
    for i in data:
        if name == data[0]:
            #print data[0]
            valuelist.append(data[1])


def interfaceRows(record):
    """
    sets start row for each Interface
    next row will be for InKbps
    next row for OutKbps
    """
    if record[0] == "INTA1":
        runrow = 1
    elif record[0] == "INTA2":
        runrow = 4
    elif record[0] == "INTA3":
        runrow = 7
    elif record[0] == "INTA4":
        runrow = 10
    return runrow


def intinbits(record):
    if record[0] == "INTA1":
        A1inbits.append(record[1])
        return A1inbits


def intoutbits(record):
    if record[0] == "INTA1":
        A1outbits.append(record[2])
        return A1outbits
# def PortArray():
#     """Determines values of ports in output"""


def createWorkbook(out_file):
    """Creates workbook and worksheet using XlsxWriter"""
    workbook = xlsxwriter.Workbook(out_file, {'strings_to_numbers': True})
    return workbook

def createWorksheet(wb):
    ws = wb.add_worksheet("Bitrates")  # would love to have timestamp
    big_num = wb.add_format({'num_format': '0'})
    ws.set_column('B:C', 18, big_num)
    # # Write header for Column Worksheet
    # ws.write('A1', "Port")
    # ws.write(0, 1, "InKbps", big_num)
    # ws.write(0, 2, "OutKbps", big_num)
    return ws

def toExcel(record):
    for interface in (record):
        print interface
    # ws.write(row, col,     interface)
    # ws.write(row, col + 1, inkbps)
    # ws.write(row, col + 2, outkbps)
    # row += 1
    # col += 2
    return

 # ws.write(1,2,"oOct")
#     row = int(rList[1])
#     column = int(rList[0])
#
#     value1 = rList[2]
#     counter2 = rList[3]
#     value2 = rList[4]
#     ws.write(column, row, value1)
#     ws.write(column, row+1, value2)
#     return



#
# def writeToExcel(rList, ws, option):
    # """
    # record = ['PortName', 'InKbps', 'OutKbps']
    # want format;
    # PortName
    #     InKbps
    #     OutKbps
    # """#
    # ws.write(1,2,"oOct")
#     row = int(rList[0])
#     column = int(rList[1])
#     value1 = rList[2]
#     ws.write(row, column, value1)
#     return
#
#
# def printList(rList):
#     return
#     for i in rList:
#         print(i)
#     return
#
#
# def print1(string, flag):
#     if flag:
#         print(string)
#
#
#
#
#
# def getPortName(arr):
#     return arr[0]
#
#
# def getQueueNum(arr):
#     return arr[3]
#
#
# def getQueueType(arr):
#     return arr[1]
#
#
# def getQueueValue(arr):
#     return arr[2]
#
#
# def getNum(str1):
#     """
#     Input: String with two numbers in it separated
#     Output: Group, two numbers
#     """
#     return re.search(r'\d+', str1).group()
#
#
# def getNums(str1):
#     return re.search(r'(\d+).* (\d+)', str1)
#
#
# def getIntPort(str):
#     # return re.search(r'(
#     return
#
#
# def isPort(port):
#     """tells you if the item is a number"""
#     if type(port) == int:
#         return True
#     else:
#         return False
#
#
# # line = "QoS Rate for port 4:"
# line = "Tx Packets:                               4"
# port = 0
# parseQueueRate(line, port, 3)
#
# k = 5
# print1(isPort(k), PRINT)
