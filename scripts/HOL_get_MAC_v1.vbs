#$language = "VBScript"
#$interface = "1.0"

crt.Screen.Synchronous = True


' This value is what triggers the script to jump out of the loop
Threshold = 3000

' Start with SecureCRT tab logged into SI4093.

Sub Main
' This is the Initial setup section. Enters priv. mode, sets terminal-len to 0, and clears counters 
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

	strLines = crt.Screen.Get2(9,1, 22,80)  ' This scrapes a section of the output. 
											' Start Row,Col, End Row,Col
											' *** Adj to get the whole section ***
	vLines = Split(strLines, vbcrlf) ' Splits section into individual lines

    For nIndex = 1 To UBound(vLines) ' an Iterator through each line
        strData = vLines(nIndex -1) & vbCrLf  ' Converting Variant() to string
		if StrComp(Left(strData, 5),VLAN) Then ' Because sometimes we get extra stuff
			HOLVal = Right(strData, 6)  ' This should be the HOL number. Will check up to 6 chars (999999)
				If Cint(HOLVal) > Threshold Then Exit DO  ' We are higher than Threshold, go get the mac-address-table			
					' MsgBox "Here's your Threshold: " & Threshold & vbcrlf & "Here's your HOL: " & HOLVal
				'End if
		End if
	Next


' If we didn't meet the threshhold, wait 5 seconds, and check again  
	crt.Sleep 5000
	LOOP

	'crt.Session.Disconnect  ' Disconnects from the SI4093 session  (optional)

' This section opens a new tab to the G8264CS  

' ***** Need to put correct values for username, password and host-ip. Also need to set path for LogFile *****  

' CHANGE VALUES!                                        *****           *****       ************
	Set tabG8264CS = crt.Session.ConnectInTab("/SSH2 /L admin /PASSWORD admin /P 22 172.70.70.21")

'This section enters priv. mode, sets terminal-len to 0, sets the log file name and location, displays mac-table
	tabG8264CS.Screen.Send "en" & chr(13)
	tabG8264CS.Screen.WaitForString "#"
	tabG8264CS.Screen.Send "terminal-len 0" & chr(13)
	tabG8264CS.Screen.WaitForString "#"
	tabG8264CS.Screen.Send "show clock" & chr(13)
	tabG8264CS.Screen.WaitForString "#"
	tabG8264CS.Session.LogFileName = "C:\Temp\%H_MAC-Table_%Y-%M-%D--%h-%m-%s.txt"  ' ***Change dir as needed****
	tabG8264CS.Session.Log True  ' Start logging
    tabG8264CS.Screen.Send "show mac-address-table" & chr(13)
	tabG8264CS.Screen.WaitForString "#"
	tabG8264CS.Session.Log False  ' Stop Logging
	tabG8264CS.Session.Disconnect  ' disconnects from the G8264CS session

	' This pops up a message informing the user that HOL Blocking was detected, and where to find the Log File  
	MsgBox "HOL Blocking detected! " &  vbcrlf & "Log file is located at"  & vbcrlf & tabG8264CS.Session.LogFileName 
End Sub

' Command used for testing: "sh int port INTA1-14 interface-counters " & chr(124) & " inc HOL" & chr(13)