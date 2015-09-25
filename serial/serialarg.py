## serialarg.py ##############
## pass arguments to script ##
##############################
from sys import argv
import serial


def sendMessage(message, connection):
	connection.write(message)

if(__name__ == "__main__"):
	script, message = argv
	connection = serial.Serial('/dev/ttyACM0', 9600)
	sendMessage(message, connection)

