## smart_temperature_sensor

import json
import random
import time
import socket
import os
import csv


DATA_DIR="./data/"
with open('config.json') as f:
	config = json.load(f)

def temperature_sensor(room, ID):
	print("starting temperature_sensor device ... Ctrl+c to quit")
	start = time.time()
	device = "smart_temperature_sensor"
	ip = "127.0.0.1"
	p = int(config[room][device]['port'][int(ID)])
	id = config[room][device]['id'][int(ID)]

	avg_temp = random.uniform(-30, 50)
	feed_start = start

	while 1:
		present_time = round(time.time(), 5)

		value = str(round(random.normalvariate(avg_temp, 10), 1)) + "Degree-Celsius"
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

