## smart_smoke_detector

import json
import random
import time
import socket
import os
import csv

DATA_DIR="./data/"

#with open('config.json') as f:
#	config = json.load(f)

def smoke_detector(room, ID):
	print "Starting Smart Smoke detector device .. press Ctrl+c to stop"
	start = time.time()
	device = "smoke_detector"
	ip = "127.0.0.1"
	id = config[room][device]['id'][int(ID)]
	p = int(config[room][device]['port'][int(ID)])

	#True for lock False for open

	water_sprinkler=False
	option=[True,False]
	door=random.choice(option)
	windows=random.choice(option)

	while 1:

		ppm=random.randint(1,400)
		
		present_time = round(time.time(), 5)
		
		#print ppm
		if ppm<80:
			door = True
			windows = True
			water_sprinkler=False

		elif ppm>=80 and ppm<250:
			door = True
			windows = True
			water_sprinkler = True

		else:
			door = False
			windows = False
			water_sprinkler = False
			print "Smoke detected Evacuate!"

		value = str(ppm) + "ppm-door-" + str(door) + "-win-" + str(windows) + "-sprk-" + str(water_sprinkler)

		message={}
		message["id"] = str(id)
		message["unix_timestamp"]=str(present_time)
		message["data_size"]=str(len(str(value)))
		message["data"]=str(value)	
		timeout = 1.0	

		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		server__add = (ip, p)
		sent = 0
		message_to_send = str(message)

		while(sent<len(message_to_send)):
			sent = sent + sock.sendto(message_to_send[sent:len(message_to_send)], server__add)	

		csv.writer(open(DATA_DIR + id + '.csv', 'ab'), delimiter = ',').writerow([present_time, value])
		time.sleep(timeout)

		if(time.time() - start > 43200):
			return 
