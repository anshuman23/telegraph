#main file
# i is system arguments iterator
# j is iterator for devices of each type

from subprocess import Popen
from time import sleep
import random
import json
import sys
from motionD import motion_detector
from temperatureS import temperature_sensor
from Smart_lights import smart_lights
from smartAC import smart_Ac
from Smoke_detector import smoke_detector

print("This is simulation of devices in the 1st room in the model house")
total_types = int(sys.argv[1])
#print(total_types)
room = "room1"

with open('config.json', 'r') as f:
	config = json.load(f)

i = 2
types_of_devices = total_types
while(types_of_devices > 0):

	ports = ["80", "3000"]
	device = str(sys.argv[i])
	config[room][device]['quantity'] = int(sys.argv[i+1])
	number_of_devices = int(sys.argv[i+1])
	#print(n)
	#print(device)
	j = 0
	config[room][device]['id'] = []
	config[room][device]['port'] = []
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

while(types_of_devices > 0):
	device = str(sys.argv[i])
	print(device)
	number_of_devices = int(sys.argv[i+1])
	j = 0

	if(device == "smart_motion_detector_camera"):
		while(number_of_devices>0):
			launch_motionD = "runp " + "motionD.py " + "motion_detector:\"" + room + "\",ID=" + str(j)
			procMD.append(Popen("xterm -e '" + launch_motionD + "'", shell = True))
			sleep(8)
			print "Started first window"

			#motion_detector("room1", j)
			number_of_devices = number_of_devices - 1
			j = j + 1

	elif(device == "smart_temperature_sensor"):
		while(number_of_devices>0):
			launch_temperatureS = "runp" + "temperatureS.py" + "temperature_sensor:\"" + room + "\",ID=" + str(j)
			procTS.append(Popen("xterm -e '" + launch_temperatureS + "'", shell = True))
			sleep(8)
			print "Started second window"

			#temperature_sensor("room1", j)
			number_of_devices = number_of_devices - 1
			j = j + 1

	elif(device == "smart_lights"):
		while(number_of_devices>0):
			launch_smart_lights = "runp" + "Smart_lights.py" + "smart_lights:\"" + room + "\",ID=" + str(j)
			procSL.append(Popen("xterm -e '" + launch_smart_lights + "'", shell = True))
			sleep(8)
			print "started Third window"

			number_of_devices = number_of_devices - 1
			j = j + 1

	elif(device == "smoke_detector"):
		while(number_of_devices>0):
			launch_smoke_detector = "runp" + "Smoke_detector.py" + "smoke_detector:\"" + room + "\",ID=" + str(j)
			procSD.append(Popen("xterm -e '" + launch_smoke_detector + "'", shell = True))
			sleep(8)
			print "started fourth window"

			number_of_devices = number_of_devices - 1
			j = j + 1

	elif(device == "smart_ac"):
		while(number_of_devices>0):
			launch_smart_ac = "runp" + "smartAC.py"+ "smart_Ac:\"" + room + "\",ID=" + str(j)
			procSA.append(Popen("xterm -e '" + launch_smart_ac + "'", shell = True))
			sleep(8)
			print "started fifth window"

			number_of_devices = number_of_devices - 1
			j = j + 1

	else:
		break

	types_of_devices = types_of_devices - 1
	i = i + 2


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
