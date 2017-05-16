import re

# Variables for Intf Counters
octets = 1
unicast = 3
broadcast = 5
multicast = 7
fc = 9
pfc = 11
discards = 13
errors = 15
vlan = 17
filterDiscards = 19
policy = 21
nfs = 23
ibp = 25
eep = 27

# Variables for Queue Stat and Rate
txPackets = 1
dPackets = 2
txBytes = 3
dBytes = 4


# Print flag
PRINT = 1


def parseIntfCounters(line, portName):
    """
    Takes a line, return parsing of show tech
    INPUT: String, String
    Output: Array of format
    [portName,counterName,value1 of counter,counter2Name,value2]
    """
    matchPort = re.compile(r'Interface statistics for port')
    matchOct = re.compile(r'Octets: +\d+ + \d+')
    matchUnicast = re.compile(r'UcastPkts: +\d+ + \d+')
    matchBroadcast = re.compile(r'BroadcastPkts: +\d+ + \d+')
    matchMilticast = re.compile(r'MulticastPkts: +\d+ + \d+')
    matchFC = re.compile(r'FlowCtrlPkts: +\d+ + \d+')
    matchPFC = re.compile(r'PriFlowCtrlPkts: +\d+ + \d+')
    matchDiscards = re.compile(r'Discards: +\d+ + \d+')
    matchErrors = re.compile(r'Errors: +\d+ + \d+')
    matchVlan = re.compile(r'VLAN Discards: +\d+ + HOL-blocking')
    matchFilter = re.compile(r'Filter Discards: +\d+ + MMU Discards:')
    matchPolicy = re.compile(r'Policy Discards: +\d+ + Cell Error Discards:')
    matchNFS = re.compile(r'Non-Forwarding State: +\d+ + MMU Aging Discards')
    matchIBP = re.compile(r'IBP/CBP Discards: +\d+ + Other Discards')
    matchEEP = re.compile(r'Empty Egress Portmap:')

    result = []
    # portNum = 0
    counter1 = None
    value1 = None
    counter2 = None
    value2 = None
    if (re.search(matchPort, line)):
        portName = re.search(r'INTA\d+|EXT\d+|\d+', line).group()
        print1("matchPort", PRINT)
        return [portName,  0, value1, counter2, value2]
    elif (re.search(matchOct, line)):
        print1("match Octects", PRINT)
        counter1 = octets

    elif (re.search(matchUnicast, line)):
        print1("matchUnicast", PRINT)
        counter1 = unicast

    elif (re.search(matchBroadcast, line)):

        counter1 = broadcast
    elif (re.search(matchMilticast, line)):

        counter1 = multicast
    elif (re.search(matchPFC, line)):
        counter1 = pfc
    elif (re.search(matchFC, line)):
        counter1 = fc
    elif (re.search(matchErrors, line)):
        counter1 = errors
    elif (re.search(matchVlan, line)):
        counter1 = vlan
    elif (re.search(matchFilter, line)):

        counter1 = filterDiscards
    elif (re.search(matchPolicy, line)):
        counter1 = policy
    elif (re.search(matchNFS, line)):
        counter1 = nfs
    elif (re.search(matchIBP, line)):
        counter1 = ibp
    # elif (re.search(matchEEP,line)):
    #    counter1 = eep
    elif (re.search(matchDiscards, line)):
        counter1 = discards
    else:
        # print1("did not match anything",PRINT)
        return [portName, counter1, value1, counter2, value2]

    # If statement below should never be true
    if counter1 == None:
        print(line)

    value = getNums(line)
    value1 = value.group(1)
    value2 = value.group(2)
    counter2 = counter1 + 1
    result = [portName, counter1, value1, counter2, value2]
    return result


def toExcelIntfCounter(rList, ws, option):
    # ws.write(1,2,"oOct")
    row = int(rList[1])
    column = int(rList[0])

    value1 = rList[2]
    counter2 = rList[3]
    value2 = rList[4]
    ws.write(column, row, value1)
    ws.write(column, row+1, value2)
    return


def writeToExcel(rList, ws, option):
    # ws.write(1,2,"oOct")
    row = int(rList[0])
    column = int(rList[1])
    value1 = rList[2]
    ws.write(row, column, value1)
    return


def printList(rList):
    return
    for i in rList:
        print(i)
    return


def print1(string, flag):
    if flag:
        print(string)


def intfCounterHeaders(ws):
    """Interface Counter Headers"""
    headers = ["inOctects", "outOctects", "inUcastPkts", "outUcastPkts", "inBroadcasts", "outBroad"]
    headers = headers + ["inMulti", 'outMulti', 'inFlowControl', 'outFlowControl', 'inPFC', 'outPFC']
    headers = headers + ['inDiscards', 'outDiscards', 'inErrors', 'outErrors', 'inVlanDisc', 'outHOL']
    headers = headers + ['inFilterDisc', 'outMmuDisc', 'inPolicyDisc', 'outCellErr', 'inNFwd']
    headers = headers + ['outMmuAging', 'inIBP']
    location = ['B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1', 'I1', 'J1']
    location = location + ['K1', 'L1', 'M1', 'N1', 'O1', 'P1', 'Q1', 'R1', 'S1', 'T1']
    location = location + ['U1', 'V1', 'W1', 'X1', 'Y1', 'Z1']

    ws.write(0, 26, "otherDisc")
    for index in range(len(headers)):
        ws.write(str(location[index]), str(headers[index]))


def queueHeaders(ws):
    """Queue Headers"""
    column = 1
    headers = ["q0TxPkts", "q0DropPkts", "q0TxBytes", "q0DropBytes"]
    headers = headers + ["q1TxPkts", "q1DropPkts", "q1TxBytes", "q1DropBytes"]
    headers = headers + ["q2TxPkts", "q2DropPkts", "q2TxBytes", "q2DropBytes"]
    headers = headers + ["q3TxPkts", "q3DropPkts", "q3TxBytes", "q3DropBytes"]
    headers = headers + ["q4TxPkts", "q4DropPkts", "q4TxBytes", "q4DropBytes"]
    headers = headers + ["q5TxPkts", "q5DropPkts", "q5TxBytes", "q5DropBytes"]
    headers = headers + ["q6TxPkts", "q6DropPkts", "q6TxBytes", "q6DropBytes"]
    headers = headers + ["q7TxPkts", "q7DropPkts", "q7TxBytes", "q7DropBytes"]
    location = ['B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1', 'I1', 'J1']
    location = location + ['K1', 'L1', 'M1', 'N1', 'O1', 'P1', 'Q1', 'R1', 'S1', 'T1']
    location = location + ['U1', 'V1', 'W1', 'X1', 'Y1', 'Z1']
    location = location + ['U1', 'V1', 'W1', 'X1', 'Y1', 'Z1']
    location = location + ['U1', 'V1']
    for index in range(len(headers)):
        ws.write(0, column, str(headers[index]))
        column = column + 1
    # ws.write(str(location[index]),str(headers[index]))


def parseQueueStat(line, portName):
    """docstring"""
    matchPort = re.compile(r'QoS Queue +(\d)')
    matchTxPkts = re.compile(r'Tx Packets: +(\d+)')
    matchQueue = re.compile(r'QoS Queue')
    matchTxPkts = re.compile(r'Tx Packets:')
    matchDroppedPkts = re.compile(r'Dropped Packets:.*(\d)')
    matchTxBytes = re.compile(r'Tx Bytes:.*(\d)')
    matchDroppedBytes = re.compile(r'Dropped Bytes:.*(\d)')

    if (re.search(matchPort, line)):
        value = getNum(line)

    return


def parseQueueRate(line, portName, queueNum):
    """
    Takes in a line, and returns a parse line
    Returns an array with format
    [portName,counterName,value of counter,queueNumber]
    """
    result = None
    value = 0
    counterType = 0
    PRINT = 0
    # Set Matches
    matchPortRate = re.compile(r'Rate for port ((\d)|(\d\d))')
    matchPortStat = re.compile(r'QoS statistics for port')
    matchTxPkts = re.compile(r'Tx Packets:.*(\d+)')
    matchQueue = re.compile(r'QoS Queue')
    matchTxPkts = re.compile(r'Tx Packets:')
    matchDroppedPkts = re.compile(r'Dropped Packets:.*(\d)')
    matchTxBytes = re.compile(r'Tx Bytes:.*(\d)')
    matchDroppedBytes = re.compile(r'Dropped Bytes:.*(\d)')

    if (re.search(matchPortRate, line)):
        # value = re.search(matchPort,line).group(1)
        print1('it is true, port is ' + str(value), PRINT)
        # value = getNum(line)
        queueNum = 0
        portName = getNum(line)
        return [portName, 0, value, queueNum]

    # Matches 'QoS statistics for port 62:'
    elif (re.search(matchPortStat, line)):
        # value = re.search(matchPort,line).group(1)
        portName = getNum(line)
        queueNum = 0
        return [portName, 0, value, queueNum]

    elif (re.search(matchQueue, line)):
        queueNum = getNum(line)
        # counterType = "QueueNum"
        # queue = value
        return[portName, counterType, value, queueNum]

    elif (re.search(matchTxPkts, line)):
        # value = re.search(matchTxPkts,line).group(1)
        value = getNum(line)
        counterType = str((4*int(queueNum)) + txPackets)
        # print1('MATCH tx pkts is ' + str(value),PRINT)

    elif (re.search(matchDroppedPkts, line)):
        value = getNum(line)
        counterType = str((4*int(queueNum)) + dPackets)
        # print1('tx pkts is ' + str(value),PRINT)

    elif (re.search(matchTxBytes, line)):
        value = getNum(line)
        counterType = str((4*int(queueNum)) + txBytes)
        print1('tx pkts is ' + str(value), PRINT)

    elif (re.search(matchDroppedBytes, line)):
        value = getNum(line)
        counterType = str((4*int(queueNum)) + dBytes)
        print1('tx pkts is ' + str(value), PRINT)

    result = [portName, counterType, value, queueNum]
    print1(result, PRINT)
    return result
# END OF PARSETUPPLE


def getPortName(arr):
    return arr[0]


def getQueueNum(arr):
    return arr[3]


def getQueueType(arr):
    return arr[1]


def getQueueValue(arr):
    return arr[2]


def getNum(str1):
    """
    Input: String with two numbers in it separated
    Output: Group, two numbers
    """
    return re.search(r'\d+', str1).group()


def getNums(str1):
    return re.search(r'(\d+).* (\d+)', str1)


def getIntPort(str):
    # return re.search(r'(
    return


def isPort(port):
    """tells you if the item is a number"""
    if type(port) == int:
        return True
    else:
        return False


# line = "QoS Rate for port 4:"
line = "Tx Packets:                               4"
port = 0
parseQueueRate(line, port, 3)
# if line is for port, return port number
# if line  is tx bytes, return (TxPkts, num)

# should I make a link list that contains
# (portNum, queueNum, tuppleName, value)

# then do a for loop that makes it go to excel


k = 5
print1(isPort(k), PRINT)
