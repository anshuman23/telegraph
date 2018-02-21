## smart_motion_detector_camera 

import random
import time
import socket
import os
import csv
import json

DATA_DIR="./data/"

with open('config.json', 'r') as f:
	config = json.load(f)


def motion_detector(room, ID):
	print "Starting smart motion detector device .. press Ctrl+c to stop"
	start = time.time()
	device = "smart_motion_detector_camera"
	ip = "127.0.0.1"
	id = config[room][device]['id'][int(ID)]
	p = int(config[room][device]['port'][int(ID)])

	motion_bool = random.choice([0,1])
	feed_start = start

	while 1:
		present_time = round(time.time(), 5)

		if(motion_bool != 0):
			fps=15
			bitrate=int(random.uniform(50000, 200000))
			value=os.urandom(bitrate/8/fps)
			timeout=float(1.0/fps)
			motion_time=float(random.uniform(1,5))
			if((time.time() - feed_start) > motion_time):
				motion_bool = 0

		else:
			value = "X"
			motion_bool = random.choice([0,1])
			timeout=float(random.uniform(1, 10))
			feed_start = time.time() + timeout


		message={}
		message["id"] = str(id)
		message["unix_timestamp"] = str(present_time)
		message["data_size"] = str(len(str(value)))
		message["data"] = str(value)


		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		server_add = (ip, p)
		sent = 0
		message_to_send = str(message)

		while(sent < len(message_to_send)):
			sent = sent + sock.sendto(message_to_send[sent:len(message_to_send)], server_add)

		csv.writer(open(DATA_DIR + id +'.csv', 'ab'), delimiter = ',').writerow([present_time, message["data_size"]])
		if(value!="X"):
			feed_data = open(DATA_DIR + id + '.mpeg2', 'ab')
			feed_data.write(str(value))
			feed_data.close

		time.sleep(timeout)

		if(time.time() - start > 43200):
			return 

