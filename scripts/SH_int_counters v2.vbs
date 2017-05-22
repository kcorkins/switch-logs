#$language = "VBScript"
#$interface = "1.0"

crt.Screen.Synchronous = True

' This automatically generated script may need to be
' edited in order to work correctly.

Sub Main
	crt.Screen.Send "en" & chr(13)
	crt.Screen.WaitForString "#"
	crt.Screen.Send "terminal-len 0" & chr(13)
	crt.Screen.WaitForString "#"
	DO
	crt.Screen.Send "show clock" & chr(13)
	crt.Screen.WaitForString "#"
	crt.Screen.Send "show inter counter " & chr(124) & " inc HOL" & chr(13)
	crt.Screen.WaitForString "#"
	crt.Sleep 5000 
	LOOP
End Sub
