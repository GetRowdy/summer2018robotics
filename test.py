#!/usr/bin/env python3
from ev3dev.ev3 import *
from time import sleep

#TODO: Add code here
def move(time, speed):
	leftM.run_timed(time_sp=time, speed_sp=speed)
	rightM.run_timed(time_sp=time, speed_sp=speed)

leftM = LargeMotor('outA')
rightM = LargeMotor('outB')

Sound.speak('Moving Forward One Second').wait()
#Forward Movement

leftM.run_timed(time_sp=1000, speed_sp=360)
rightM.run_timed(time_sp=1000, speed_sp=360)

leftM.wait_while('running')
rightM.wait_while('running')


print ("left wheel speed (leftM. speed_sp) = " + str(leftM.speed_sp) + " and  right wheel speed (rightM.speed_sp) = " + str(rightM.speed_sp))

sleep(1) #wait for movement forward

#Reverse Movement
leftM.run_timed(time_sp=1000, speed_sp=-360)
rightM.run_timed(time_sp=1000, speed_sp=-360)

leftM.wait_while('running')

Sound.beep()
#Left Turn
rightM.run_timed(time_sp=1000, speed_sp=150)


