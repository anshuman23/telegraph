#main file
# i is system arguments iterator
# j is iterator for devices of each type

from subprocess import Popen
from time import sleep
import random
import json
import sys
from motionDetector import motion_detector
from temperatureSensor import temperature_sensor
from smartLights import smart_lights
from smartAC import smart_ac
from smokeDetector import smoke_detector
from smartLock import smart_lock
from smartToaster import smart_toaster
from sys import platform

print("This is simulation of devices in the 1st room in the model house")
total_types = int(sys.argv[1])
room = "room1"

## setting terminal varianle acc to system
if platform == "linux" or platform == "linux2":
	terminal = "gnome-terminal"

elif platform == "darwin":
	terminal = "xterm"


with open('config.json', 'r') as f:
	config = json.load(f)

i = 2
types_of_devices = total_types
while(types_of_devices > 0):

	ports = ["80", "3000"]
	device = str(sys.argv[i])

	config[room][device]['id'] = []
	config[room][device]['port'] = []
	config[room][device]['quantity'] = 0
	config[room][device]['quantity'] = int(sys.argv[i+1])
	number_of_devices = int(sys.argv[i+1])
	#print(n)
	#print(device)
	j = 0
	while(number_of_devices > 0):

		config[room][device]['id'].append(device + "-" + str(j))
		r = random.choice(ports)
		config[room][device]["port"].append(r)
		ports.remove(r) 
		j = j + 1
		number_of_devices = number_of_devices - 1


	with open('config.json', 'w') as f:
		json.dump(config, f, indent = 4) ## prety print changes

	i = i+2
	types_of_devices = types_of_devices - 1	

types_of_devices = total_types
i = 2

procMD = [] # List of Motion Detector processes
procTS = [] # List of Temperature Sensor processes
procSL = [] # List of Smart Light processes
procSD = [] # List of Smoke detector processes
procSA = [] # List of smart air conditionner processes
procSLo = [] #List of smart locks
procST = [] # List of smart toasters


while(types_of_devices > 0):
	device = str(sys.argv[i])
	print(device)
	number_of_devices = int(sys.argv[i+1])
	j = 0

	if(device == "smart_motion_detector_camera"):
		while(number_of_devices>0):
			launch_motionD = "runp " + "motionDetector.py " + "motion_detector:\"" + room + "\",ID=" + str(j)
			procMD.append(Popen(terminal + " -e '" + launch_motionD + "'", shell = True))
			print "Started first window"
			sleep(5)

			#motion_detector("room1", j)
			number_of_devices = number_of_devices - 1
			j = j + 1

	elif(device == "smart_temperature_sensor"):
		while(number_of_devices>0):
			launch_temperatureS = "runp " + "temperatureSensor.py" + "temperature_sensor:\"" + room + "\",ID=" + str(j)
			procTS.append(Popen(terminal + " -e '" + launch_temperatureS + "'", shell = True))
			print "Started second window"
			sleep(5)

			#temperature_sensor("room1", j)
			number_of_devices = number_of_devices - 1
			j = j + 1

	elif(device == "smart_lights"):
		while(number_of_devices>0):
			launch_smart_lights = "runp " + "smartLights.py" + "smart_lights:\"" + room + "\",ID=" + str(j)
			procSL.append(Popen(terminal + " -e '" + launch_smart_lights + "'", shell = True))
			print "started Third window"
			sleep(5)

			number_of_devices = number_of_devices - 1
			j = j + 1

	elif(device == "smoke_detector"):
		while(number_of_devices>0):
			launch_smoke_detector = "runp " + "smokeDetector.py" + "smoke_detector:\"" + room + "\",ID=" + str(j)
			procSD.append(Popen(terminal + " -e '" + launch_smoke_detector + "'", shell = True))
			print "started fourth window"
			sleep(5)

			number_of_devices = number_of_devices - 1
			j = j + 1

	elif(device == "smart_ac"):
		while(number_of_devices>0):
			launch_smart_ac = "runp " + "smartAC.py"+ "smart_ac:\"" + room + "\",ID=" + str(j)
			procSA.append(Popen(terminal + " -e '" + launch_smart_ac + "'", shell = True))
			print "started fifth window"
			sleep(5)

			number_of_devices = number_of_devices - 1
			j = j + 1

	elif(device == "smart_lock"):
		while(number_of_devices>0):
			launch_smart_lock = "runp " + "smartLock.py" + "smart_lock:\"" + room + "\",ID=" + str(j)
			procSLo.append(Popen(terminal + " -e '" + launch_smart_lock + "'", shell = True))
			print "starting sixth window"
			sleep(5)

			number_of_devices = number_of_devices - 1
			j = j + 1

	elif(device == "smart_toaster"):
		while(number_of_devices>0):
			launch_smart_lock = "runp " + "smartToaster.py" + "smart_toaster:\"" + room + "\",ID=" + str(j)
			procST.append(Popen(terminal + " -e '" + launch_smart_lock + "'", shell = True))
			print "starting seventh window"
			sleep(5)

			number_of_devices = number_of_devices - 1
			j = j + 1

	else:
		break

	types_of_devices = types_of_devices - 1
	i = i + 2




sleep(10) ## let processes run for some time before terminating


## Terminating parallel proccesses ##



a = len(procMD)
b = len(procTS)
c = len(procSL)
d = len(procSD)
e = len(procSA)
i = 0
j = 0
k = 0
l = 0
m = 0

while (a > 0):
	procMD[i].terminate()
	procMD[i].kill()
	i = i + 1
	a = a - 1

while(b > 0):
	procTS[j].terminate()
	procTS[j].kill()
	j = j + 1
	b = b - 1

while(c > 0):
	procSL[k].terminate()
	procSL[k].kill()
	k = k + 1
	c = c - 1

while(d > 0):
	procSD[l].terminate()
	procSD[l].kill()
	l = l + 1
	d = d - 1

while(e > 0):
	procSA[m].terminate()
	procSA[m].kill()
	m = m + 1
	e = e - 1

print "terminating processes" 
