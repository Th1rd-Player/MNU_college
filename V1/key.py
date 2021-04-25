import keyboard
import time
import os
while True:
	if keyboard.is_pressed("Ctrl+Shift+s"):
		keyboard.press_and_release('Ctrl+s')
		time.sleep(1)
		keyboard.press_and_release('Alt+F4')
		time.sleep(3)	
	elif keyboard.is_pressed("a+l+f"):
		os.startfile(r'F:\O.S.Vitual')
	elif keyboard.is_pressed("s+t+o+p"):
		break
		exit()

		
