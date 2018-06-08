
#!/usr/bin/env python3
from ev3dev.ev3 import *
from time import sleep

leftM = LargeMotor('outA')
rightM = LargeMotor('outB')

def move(time, speed):
	print("time: " + str(time) + " -- speed:" + str(speed))
	leftM.run_timed(time_sp=time, speed_sp=speed)
	rightM.run_timed(time_sp=time, speed_sp=speed)
	leftM.wait_while('running')
	print("Movement Complete")
	Sound.beep()

def turn(time, speed, myDir):
	print("time: " + str(time) + " -- speed: " + str (speed) + " -- direction: " + str(myDir))
	if myDir === left:
		leftM.run_timed(time_sp=time, speed_sp=0)
		rightM.run_timed(time_sp=time, speed_sp=speed)
		leftM.wait_while('running')
		Sound.beep()
	if myDir === right:
		leftM.run_timed(time_sp=time, speed_sp=speed)
		rightM.run_timed(time_sp=time, speed_sp=0)
		leftM.wait_while('running')
		Sound.beep()
	else:
		leftM.run_timed(time_sp=time, speed_sp=speed)
		rightM.run_timed(time_sp=time, speed_sp=speed)
		leftM.wait_while('running')
		Sound.beep()

def textSpeech(text):
	print("Speaking the following: " + str(text))
	Sound.speech(str(text))

#forward
move(1000, 360)
#backward
move(1000,-360)
#left turn
turn(1000,360,left)
#right turn
turn(1000,360,right)
#no turn (test case)
turn(1000,360, up)
#text-to-speech
textSpeech(test)

