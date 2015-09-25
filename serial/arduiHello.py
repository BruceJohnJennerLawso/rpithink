## arduiHello.py ##############
## see what the arduino has to ## say right now #############################################

import serial

if(__name__ == "__main__"):
	connection = serial.Serial('/dev/ttyACM0', 9600)
	while True:
		print connection.readline()
