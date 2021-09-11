import os
import pyttsx3
Amisha=pyttsx3.init()
voice=Amisha.getProperty('voices')
Amisha.setProperty('voice',voice[1].id)
programToRun=0
while True:
	print(" \nchrome")
	print(" calculator")
	print(" window media player")
	print(" camera\n type exit if u want to exit")
	Text=input("From the list above what want You want to run:")
	programList=['chrome','calculator','wmplayer','window media player','player','media','google chrome','camera']
	i=0
	if "exit" in Text or "quit" in Text:
		exit()
	elif "don't" not in Text and "do not" not in Text:
		while i<len(programList):
			if programList[i] in Text:
				programToRun=programList[i]
				if programToRun == 'chrome' or programToRun=='google chrome':
					website=input("enter the website u want to run:")
					print("opening website")
					Amisha.say("opening website")
					Amisha.runAndWait()
					con="start chrome "+website
					os.system(con)
					break
				elif programToRun=='calculator' or programToRun=='calc':
					print("opening calculator")
					Amisha.say("opening calculator")
					Amisha.runAndWait()
					os.system("calc")
					break
				elif programToRun=='player' or programToRun=='media' or programToRun=='wmplayer' or programToRun=='window media player':
					print("opening window media player")
					Amisha.say("opening window media player")
					Amisha.runAndWait()
					os.system("start wmplayer")
					break
				elif programToRun=='camera':
					print("opening camera to click photo")
					Amisha.say("openeing camera to click photo")
					Amisha.runAndWait()
					os.system("start microsoft.windows.camera:")
					break		
			else:
				i=i+1
		else:		
			print("Please enter the correct name of the Application you want to run")						
else:
	print("Please tell what you want to open & not what you don't want too ")
				
