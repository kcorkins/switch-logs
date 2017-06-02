#$language = "VBScript"
#$interface = "1.0"

crt.Screen.Synchronous = True


' This value is what triggers the script to jump out of the loop and get show-tech
Threshold = 300000

' Start with SecureCRT tab logged into SI4093.

Sub Main
' This is the Initial setup section. 
' Enables logging (be sure to set the desired log location)  
' Enters priv. mode, sets terminal-len to 0, and clears counters 
	'crt.Session.Log True  ' Start logging, If we're not logging, the pop-up needs to be changed!
	'crt.Session.LogFileName = "C:\Temp\%H_SI4093-HOL_%Y-%M-%D--%h-%m-%s.txt"  ' ***Change dir as needed****
	crt.Screen.Send "en" & chr(13)
	crt.Screen.WaitForString "#"
	crt.Screen.Send "terminal-len 0" & chr(13)
	crt.Screen.WaitForString "#"
	crt.Screen.Send "clear counters" & chr(13)
	crt.Screen.WaitForString "#"
	
' This "DO-LOOP" section shows Interface counters and scrapes the values for comparison, Loops every 5 secs.

	DO
	crt.Screen.Send "show clock" & chr(13) 'Puts a timestamp in the log  
	crt.Screen.WaitForString "#"
	crt.Screen.Send "show inter counter " & chr(124) & " inc HOL" & chr(13)
	crt.Screen.WaitForString "#"
	

' Compare the HOL number to the threshold 

	strLines = crt.Screen.Get2(34,1, 61,80)  ' This scrapes a section of the output. 
											 ' Start Row,Col, End Row,Col
											 ' *** Adj to get the whole section ***
	vLines = Split(strLines, vbcrlf) ' Splits section into individual lines
    For nIndex = 1 To UBound(vLines) ' an Iterator through each line
        strData = vLines(nIndex -1) & vbCrLf  ' Converting Variant() to string
		if StrComp(Left(strData, 4),"VLAN") = 0 Then ' Because sometimes we get extra stuff
			HOLVal = Right(strData, 7)  ' This should be the HOL number. Will check up to 7 chars (9999999)
				If Cint(HOLVal) > Threshold Then Exit DO 
					'We are higher than Threshold, go get the mac-address-table			
					'MsgBox "Threshold: " & Threshold & vbcrlf & "HOL: " & HOLVal
				End if
		End if
	Next


' If we didn't meet the Threshhold, wait 5 seconds, and check again  
	crt.Sleep 5000
	LOOP

	'crt.Session.Disconnect  ' Disconnects from the SI4093 session  (optional)
	'crt.Session.Log False  ' Stop logging on SI4093

' This section opens a new tab to the G8264CS  

' ***** Need to put correct values for username, password and host-ip. Also need to set filename for show-tech *****  

'   CHANGE VALUES!                                      *****           *****       ************
	Set tabG8264CS2A = crt.Session.ConnectInTab("/SSH2 /L ***** /PASSWORD ***** /P 22 10.64.198.186")

'This section enters priv. mode, sets terminal-len to 0, sets the log file name and location, displays mac-table
	tabG8264CS2A.Screen.Send "en" & chr(13)
	tabG8264CS2A.Screen.WaitForString "#"
	tabG8264CS2A.Screen.Send "terminal-len 0" & chr(13)
	tabG8264CS2A.Screen.WaitForString "#"
	tabG8264CS2A.Screen.Send "show clock" & chr(13)
	tabG8264CS2A.Screen.WaitForString "#"
	                                              '************
    tabG8264CS2A.Screen.Send "copy tech tftp address xxx.xxx.xxx.xxx filename %H_Show-Tech_%Y-%M-%D--%h-%m-%s.txt mgt-port"
	tabG8264CS2A.Screen.WaitForString "#"
	tabG8264CS2A.Session.Disconnect  ' disconnects from the G8264CS session

	' This pops up a message informing the user that HOL Blocking was detected, and where to find the Log File  
	MsgBox "HOL Blocking detected! " & vbcrlf _ 
	& "Please send show-tech file" & vbcrlf _ 
	& "and SI4093 log to Lenovo" & vbcrlf _
	& "Log file is located at" & vbcrlf _
	& crt.Session.LogFileName 
End Sub

' Command used for testing: "sh int port INTA1-14 interface-counters " & chr(124) & " inc HOL" & chr(13)