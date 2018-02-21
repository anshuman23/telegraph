
import os
import csv
import json
import time
import random
import socket

# X signifies abruplty stopping of toaster

DATA_DIR="./data/"

with open('config.json', 'r') as f:
	config = json.load(f)

def smart_toaster(room, ID):

	print "Simulating smart toaster device ... press ctrl + C to stop"
	ip = "127.0.0.1"
	device = "smart_toaster"
	id = config[room][device]['id'][str(ID)]
	p = config[room][device]['port'][str(ID)]
	
	start = time.time()

	while 1:
		
		timer = random.choice([1, 2, 3, 4])
		timer_store = timer
		present_time = round(time.time(), 5)
		overheating = random.choice([0, 1])

		while timer!=0:
			if(overheating):
				value = 'X'
				break

			timer -= 1

		if(not overheating):
			value = str(timer_store) + " min"

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
		time.sleep(1)

		if(time.time() - start > 43200):
			return 







