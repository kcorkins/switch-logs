import csv
import re
import sys
from functions import *
import xlsxwriter


def queueStatsToExcel(fileName, excelName):

    fileR = open(fileName)
    fileLines = fileR.readlines()
    workbook = xlsxwriter.Workbook(str(excelName), {'strings_to_numbers': True})
    ws = workbook.add_worksheet()
    ws.set_column('B:AG', 12)
    queueNum = 0
    row = 0
    portName = 0
    resultList = []
    PRINT = 0
    PRINTP = 0

    ### Start of loop
    queueNum = 0
    portNum = 888
    resultList = []
    portName = 0
    NOQUEUE = 999
    queueNum = NOQUEUE

    for line in fileLines:

        #print("currentline is " + line)
        resultList = parseQueueRate(line,portName,queueNum)
        #portName = getPortName(resultList)
        queueType = getQueueType(resultList)
        queueNum = getQueueNum(resultList)
        #print(str(portName),PRINT)
        # Check if the portName is null, if it is then
        # we have not started looking at intf counters yet
        if (int(resultList[0]) == 0):
            print1("portname is null",PRINT)
            continue

        # Check if we are parsing info for a new port
        if (str(portName) != str(resultList[0])):
            print1("portname not equal to " + str(resultList[0]),PRINT)
            row = row + 1
            portName = resultList[0]
            # Write the portName in the excel
            print1("about to write " + resultList[0] + "row " + str(row),PRINT)
            # maybe ws.write(row,0,portName) should work as well
            ws.write(row,int(resultList[1]),portName)
            continue

        # Check if this is not a counter line
        if queueType == 0:
            print1("queuetype is zero",PRINT)
            continue

        #print("TOTAL RETULT IS \n " + str(resultList) + "row " + str(row))
        resultList[0] = row
        writeToExcel(resultList,ws,1)
    ### end of loop

    # Write the header in Excel
    queueHeaders(ws)


    # Closing file
    #outputFile.close()
    print1("TOTAL RETULT IS \n " + str(resultList),PRINT)
    workbook.close()
    fileR.close()

if __name__ == "__main__":
    file_name = sys.argv[1]
    input_name = file_name.rsplit('.', 1)
    out_name = str(input_name[0]) + ".xlsx"
    # First Arg is the name of the file to be parse
    # Second arg is the name ouf the excel file to be outputed
    # queueStatsToExcel("queue_rate_output.txt","rate.xlsx")
queueStatsToExcel(file_name, out_name)
