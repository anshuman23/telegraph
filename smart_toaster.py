## smart_toaster

import json
import random
import time
import socket
import os
import csv

DATA_DIR="./data/"
#with open('config.json') as f:
#	config = json.load(f)

def timer(n):
	print "Timer set for "+str(n)+" Minutes."
	mins = 0
		# Loop until we reach n minutes running
	while mins != n:
		# Sleep for a minute	
		time.sleep(60)
		# Increment the minute total
		mins += 1


def smart_toaster(room, ID):
	print "Starting Smart toaster device .. press Ctrl+c to stop"
	start = time.time()
	device = "smart_toaster"
	ip = "127.0.0.1"
	id = config[room][device]['id'][int(ID)]
	p = int(config[room][device]['port'][int(ID)])
	

	choice=random.randint(1,2)

	while 1:
		if(choice==1):
			print "Setting Timer for toasting"
			n=random.randint(1,5)		
			timer(n)
			value='1:'+str(n)
			
		else:
			print "Starting Toaster . Press ctrl+c to switch off"		
			value:'2'+"self"			

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

