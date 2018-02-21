## smart_lights

import json
import random
import time
from time import sleep
import socket
import os
import csv


DATA_DIR="./data/"

with open('config.json') as f:
	config = json.load(f)


def smart_lights(room, ID):

	start = time.time()
	device = "smart_lights"
	ip = "127.0.0.1"
	#p = 3000 testing purpose
	#id = "smart_lights_0" testing purpose
	p = int(config[room][device]['port'][int(ID)])
	id = config[room][device]['id'][int(ID)]

	
	feed_start = start
	Lights=0


	while 1:
		present_time = round(time.time(), 5)

		motion_bool = random.choice([0,1]) #Will Be using Anshuman's Code Variable to Detect Motion

		Availability_of_daylight=random.randrange(0,100)
		Bluelight_content=random.randrange(0,100)
		Daylight_simulation=random.randrange(0,100)
		Dynamic_lighting=random.randrange(0,100)
		Tunable_white=random.randrange(0,100)
		illumination_of_room_surfaces=random.randrange(0,100)

		Luminosity=0.2*Availability_of_daylight
		Luminosity+=0.1*Bluelight_content
		Luminosity+=0.2*Daylight_simulation
		Luminosity+=0.2*Dynamic_lighting
		Luminosity+=0.2*Tunable_white
		Luminosity+=0.1*illumination_of_room_surfaces

		if(motion_bool==0):
			Lights=0
		else:
			Lights=1
			print "Current Brightness Set to "+ str(Luminosity)+"%"


		value = str(Luminosity)
		timeout = 1.0

		message={}
		message["id"] = str(id)
		message["unix_timestamp"]=str(present_time)
		message["data_size"]=str(len(str(value)))
		message["data"]=str(value)

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

	
		
