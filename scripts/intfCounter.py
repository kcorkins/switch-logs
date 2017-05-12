import csv
import re
from functions import *
import xlsxwriter

# Name of the file to be read
#fileNameR = "intfCountersLog.txt"
#fileNameR = "si4093_sh_tech.log"
#fileNameR = "8264_tech.txt"
#fileR = open(fileNameR)
#fileLines = fileR.readlines()
#maxLines = len(fileLines)

# Excel file where info is gonna be written
#workbook = xlsxwriter.Workbook('t1.xlsx')
#ws = workbook.add_worksheet()

# Print flag


### Start of loop


def intfCountersToExcel(fileName,excelName):

    fileR = open(fileName)
    fileLines = fileR.readlines()
    workbook = xlsxwriter.Workbook(str(excelName))
    ws = workbook.add_worksheet()
    queueNum = 0
    row = 0
    portName = 0
    resultList = []
    PRINT = 0
    
    for line in fileLines:
        print1("currentline is " + line,PRINT)

        # Format of resultList is
        # [portName,inCounter,inValue,outCounter,outValue]
        resultList = parseIntfCounters(line,portName)
        counter1 = resultList[1]

        # Check if we are interested in parsing this line
        if (str(resultList[0]) == None):
            continue

        # Check if we need to update the port number being parse
        if (str(portName) != str(resultList[0])):
            #print("portname not equal to " + str(resultList[0]))
            row = row + 1
            portName = resultList[0]
            # Write the portName in the excel
            print1(resultList[0] + "row " + str(row),PRINT) 
            ws.write(row,int(resultList[1]),portName)
            continue
    
        # Check if this is not a counter line
        if counter1 == None:
            continue
                
   
        resultList[0] = row
        # Writes to excel using method 0
        toExcelIntfCounter(resultList,ws,1)
        #print("list " + i + " \n " + resultList)
    
    ### end of loop

    # Writing headers
    intfCounterHeaders(ws)
#headers = ["inOctects","outOctects","inUcastPkts","outUcastPkts","inBroadcasts","outBroad"]
#headers = headers + ["inMulti",'outMulti','inFlowControl','outFlowControl','inPFC','outPFC']
#headers = headers + ['inDiscards','outDiscards','inErrors','outErrors','inVlanDisc','outHOL']
#headers = headers + ['inFilterDisc','outMmuDisc','inPolicyDisc','outCellErr','inNFwd']
#headers = headers + ['outMmuAging','inIBP']
#location = ['B1','C1','D1','E1','F1','G1','H1','I1','J1']
#location = location + ['K1','L1','M1','N1','O1','P1','Q1','R1','S1','T1']
#location = location + ['U1','V1','W1','X1','Y1','Z1']

#ws.write(0,26,"otherDisc")
#for index in range(len(headers)):
#    ws.write(str(location[index]),str(headers[index]))

              
# Closing file
#outputFile.close()
    workbook.close()
    fileR.close()
