## loadmonitor.py ############
## pass arguments to script ##
##############################
from sys import argv
import serial
import time
import psutil


def sendMessage(message, connection):
	connection.write(message)

def getCPULoad(core=-1):
	loads = psutil.cpu_percent(interval=1, percpu=True)
	output = sum(loads)/float(len(loads))
	## average out the loads across all cpus 
	if(core==-1):
		return output
	else:
		if(core >= len(loads)):
			## we requested a core that doesnt actually exist, probably
			## like core 4 on a core 2 duo
			print "core #%i does not exist, falling back to average load %f" % (core, output) 
			return output
		else:
			output = loads[core-1]
			return output
		
		
if(__name__ == "__main__"):
	##script, message = argv
	connection = serial.Serial('/dev/ttyACM0', 9600)	
	dt = 0.0
	lastTime = time.time()
	while(True):
		dt += time.time() - lastTime
		## find out how long its been since the start of the last loop
		##print "dt %f" % dt
		if(dt >= 5000000):
			currentLoad = getCPULoad()
			strOutput = "%.3f\n" % round(currentLoad, 3)
			print strOutput, len(strOutput)
			sendMessage(strOutput, connection)
			##print "sending message '%f'" % currentLoad
			## looks good to me
			dt = 0.0
