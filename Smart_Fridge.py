#Smart_Fridge
import json
import random
import time
import socket
import os
import csv


'''
Fridge is Divided into Different Zones
1. The door:Warmest part of the fridge and subject to the most temperature fluctuations, so avoid storing highly perishable foods on the door
2. Upper shelves:Usually constant in temperature. Use them for dairy products, drinks, containers of leftovers
3. Bottom shelf:This is often the coldest spot in the fridge. It's a good place to store meat, fish, and eggs
4. Crisper drawers:Drawers do tend to retain some moisture, though, which is good for produce
'''


Temperature_of_Zones={'1':6,'2':4,'3':2,'4':-2}

def Water_Dispenser(Quantity):
	print "Please Position your Bottle"
	print "Filling "+str(Quantity)+" Litres"

def Find_Zone(Find):
	Zone={'Fruits':'Shelf'} #Will Add More Items Later

	if(Zone.has_key(Find)==True):
		print "Commodity Should be placed in "+Zone[Find]
		return str(Zone[Find])
	else:
		print "Commodity Not Available in General List of Items!"
		return "NA"

def Adjust_Temperature(Zone,Temp):
	Temperature_of_Zones[Zone]=Temp
	print "Temperature adjusted to "+str(Temp)+" degree celsius for Zone "+str(Zone)	



def smart_fridge(room, ID):

	start = time.time()
	device = "smart_fridge"
	ip = "127.0.0.1"
	id = config[room][device]['id'][int(ID)]
	p = int(config[room][device]['port'][int(ID)])

	


	while 1:
		print "\n"
		print "Select Among the Options:"
		print "1. Water Dispenser"
		print "2. Smart Zone Finder"
		print "3. Adjust Temperature"
		print "4. Exit"

		present_time = round(time.time(), 5)
		
	
		option=[1,2,3]
		choice=3#random.choice(option)
		#print choice

		if (choice==1):

			Quantity=random.randint(1,100)
			Water_Dispenser(Quantity)
			value='1:'+str(Quantity)			

		elif (choice==2):
			Find=raw_input("Enter the Commodity for which you want to find the Appropriate Zone in the Refrigerator:")
			value='2:'+str(Find_Zone(Find))


		elif(choice==3):
				Zone=random.randint(1,4)
				Temp=random.randint(-4,8)
				Adjust_Temperature(Zone,Temp)
				value='3:'+str(Zone)+str(Temp)

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
