import re
import xlsxwriter

valuelist = []
item = []
portlist = []

def cleanup(line):
    """does some basic restructuring of the incoming line of text"""
    raw_str = ''.join(line)  # convert each word in list to strings
    str1 = stripESC(raw_str)  # calls the function to strip ESC codes
    return str1


def stripESC(raw_str):
    """Strips Escape codes from captured text"""
    ansi_escape = re.compile(r'(\x9B|\x1B\[)[0-?]*[ -\/]*[@-~]')
    str1 = ansi_escape.sub('', raw_str)
    return str1


def parseBitRateCounters(line):
    """
    Takes a line, return parsing of bitrate counters
    INPUT: Line from input file, String
    Output: List, of format; [portName, InBits, OutBits]
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


def getresults(port):
    """
    Currently does nothing. Was my original list of list for-loop
    takes portname, and list of results,
    loops through each portname. Then requests the data points
    """
    #for name in portname:

    #valuelist.append(port)
        #invalues(name, data)
        # print valuelist
        #del valuelist[:]  # clear list for next run - also deletes last time
        # print valuelist
    return valuelist


def invalues(port, data):
    """
    loops through data records
    if the portname matches the portname in the data record
    grab the data value and append it to the list
    """
    valuelist.append(port)  # start the row with portname. Col = A
    valuelist.append("In Kbps")  # Col B for the type of info
    for i, item in enumerate(data):
        rec = data[i]  # pull the next data record
        if port == item[0]:  # the first string in the rec is portname
            valuelist.append(rec[1])  # rec[1] is the InKbps value
    return valuelist


def outvalues(port, data):
    """
    loops through data records
    if the portname matches the portname in the data record
    grab the data value and append it to the list
    """
    valuelist.append(port)  # start the row with portname. Col = A
    valuelist.append("Out Kbps")  # Col B for the type of info
    for i, item in enumerate(data):
        rec = data[i]  # pull the next data record
        if port == item[0]:  # the first string in the rec is portname
            valuelist.append(rec[2])  # rec[2] is the OutKbps value
    return valuelist


def createWorkbook(out_file):
    """Creates workbook and worksheet using XlsxWriter"""
    workbook = xlsxwriter.Workbook(out_file, {'strings_to_numbers': True})
    return workbook

def createWorksheet(wb):
    ws = wb.add_worksheet("Bitrates")  # would love to have timestamp
    big_num = wb.add_format({'num_format': '0'})  # Not yet working
    # ws.set_column(row, col, 18, big_num)
    return ws


def toExcel(ws, valuelist, row, col):
    """Takes the string (valuelist) and writes it to worksheet"""
    ws.set_column(row, col, 18)
    for value in (valuelist):
        ws.write(row, col, value)
        col += 1
    return  # implicit, but here for completeness
