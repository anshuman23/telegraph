## smart_AC device

import json
import time
import socket
import os
import csv
import random

DATA_DIR="./data/"

#with open('config', 'r') as f:
#	config = json.load(f)


def smart_Ac(room, ID):
	print "starting smart Air conditioning device.. press ctrl+C to stop"
	start = time.time()
	device = "smart_ac"
	ip = "127.0.0.1"
	id = config[room][device]['id'][int(ID)]
	p = config[room][device]['port'][int(ID)]

	desired_temp = random.randint(16, 40)
	room_temperature = random.randint(-10, 50)

	while 1:

		present_time = round(time.time(),5)

		if(desired_temp < room_temperature):
			room_temperature = random.randint(-10, room_temperature)
			value = "cool" + str(room_temperature)

		elif(desired_temp > room_temperature):
			room_temperature = random.randint(room_temperature, 50)
			value = "hot" + str(room_temperature)

		else:
			room_temperature = random.randint(-10, 50)
			value = "eco-sleep" + str(room_temperature)

		message = {}
		message["id"] = str(id)
		message["timestamp"] = str(present_time)
		message["data_size"] = str(len(str(value)))
		message["data"] = str(value)

		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

		server__add = (ip, p)
		sent = 0
		message_to_send = str(message)
		while(sent<len(message_to_send)):
			sent = sent + sock.sendto(message_to_send[sent:len(message_to_send)], server__add)

		csv.writer(open(DATA_DIR + id + '.csv', 'ab'), delimiter = ',').writerow([present_time, value])
		time.sleep(1)
		if(time.time() - start > 43200):
			return 

