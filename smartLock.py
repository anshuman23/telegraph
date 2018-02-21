
import os
import json
import time
import random
import csv
import random
import socket

## 0 signifies lock and 1 signifies on

DATA_DIR="./data/"

with open('config.json', 'r') as f:
	config = json.load(f)

def smart_lock(room, ID):

	print "Simulating smart lock ... press ctrl + C to exit"

	start = time.time()
	device = "smart_lock"
	ip = "127.0.0.1"
	id = config[room][device]['id'][int(ID)]
	p = config[room][device]['port'][int(ID)]

	lock = random.choice([0, 1])

	while 1:

		present_time = round(time.time(), 5)

		externalSignal = random.choice([0, 1]) ## variable to be changed by other smart devices when needed

		if externalSignal != lock:
			lock = externalSignal
			value = str(lock)

		else:
			value = "sleep"


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


