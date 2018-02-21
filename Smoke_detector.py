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

#True for Lock and False for Open
water_sprinkler=False
option=[True,False]
door=random.choice(option)
windows=random.choice(option)

def timer(n):
	print "Timer set for "+str(n)+" Minutes."
	print "Please Evacuate!"
	mins = 0
		# Loop until we reach n minutes running
	while mins != n:
		# Sleep for a minute	
		time.sleep(60)
		# Increment the minute total
		mins += 1
	windows=True
	door=True
	water_sprinkler=True

def smart_smoke_detector(room, ID):
	print "Starting Smart Smoke detector device .. press Ctrl+c to stop"
	start = time.time()
	device = "smoke_detector"
	ip = "127.0.0.1"
	id = config[room][device]['id'][int(ID)]
	p = int(config[room][device]['port'][int(ID)])
	ppm=random.randint(1,500)

	while 1:
		
		present_time = round(time.time(), 5)
		
		#print ppm
		if ppm<70:
			timer(60)
			water_sprinkler=False
			continue
		elif ppm>=70 and ppm<150:
			timer(10)		
			break
		elif ppm>=150 and ppm<400:
			timer(4)
			break
		else:
			break

		message={}
		message["id"] = str(id)
		message["unix_timestamp"]=str(present_time)
		message["data_size"]=str(len(str(value)))
		message["data"]=str(value)
		value = str(ppm) + "ppm"	
		timeout = 1.0	

		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		server__add = (ip, p)
		sent = 0
		message_to_send = str(message)

		while(sent<len(message_to_send)):
			sent = sent + sock.sendto(message_to_send[sent:len(message_to_send)], server__add)	

		csv.writer(open(DATA_DIR + id + '.csv', 'ab'), delimiter = ',').writerow([present_time, value])
		time.sleep(timeout)
