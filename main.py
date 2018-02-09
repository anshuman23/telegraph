#main file

from subprocess import Popen
from time import sleep
import random
import json
import sys
from motionD import motion_detector
from temperatureS import temperature_sensor

print("This is simulation of devices in the 1st room in the model house")
total_types = int(sys.argv[1])
room = "room1"

with open('config.json', 'r') as f:
	config = json.load(f)

i = 2
t = total_types
while(t > 0):

	ports = ["80", "3000"]
	device = str(sys.argv[i])
	config[room][device]['quantity'] = int(sys.argv[i+1])
	n = int(sys.argv[i+1])
	j = 0
	config[room][device]['id'] = []
	config[room][device]['port'] = []
	while(n > 0):

		config[room][device]['id'].append(device + "-" + str(j))
		r = random.choice(ports)
		config[room][device]["port"].append(r)
		ports.remove(r) 
		j = j + 1
		n = n-1


	with open('config.json', 'w') as f:
		json.dump(config, f)

	i = i+2
	t = t - 1	

t = total_types
i = 2

procMD = []
procTS = []

while(t>0):
	device = str(sys.argv[i])
	n = int(sys.argv[i+1])
	j = 0

	if(device == "smart_motion_detector_camera"):
		while(n>0):
			launch_motionD = "runp " + "motionD.py " + "motion_detector:" + room + ",ID=" + str(j)
			procMD.append(Popen("gnome-terminal -e '" + launch_motionD + "'", shell = True))

			#motion_detector("room1", j)
			n = n - 1
			j = j + 1

	elif(device == "smart_temperature_sensor"):
		while(n>0):
			launch_temperatureS = "runp " + "temperatureS.py " + "temperature_sensor:" + room + ",ID=" + str(j)
			procTS.append(Popen("gnome-terminal -e '" + launch_temperatureS + "'", shell = True))
			
			#temperature_sensor("room1", j)
			n = n - 1
			j = j + 1

	else:
		break

	t = t-1
	i = i+2

a = len(procMD)
b = len(procTS)
i = 0
j = 0

while (a > 0):
	procMD[i].terminate()
	procMD[i].kill()
	i = i+1
	a = a-1

while(b>0):
	procTS[j].terminate()
	procTS[j].kill()
	j = j+1
	b = b-1





##temperature_sensor(sys.argv[4], sys.argv[5], sys.argv[6])
