import random
import time
import socket
import os
import csv

DATA_DIR="./data/"            
    

def runSim(argv):
    print "Starting device simulation...To stop the simulation press Ctrl+c"
    start = time.time()
    device = argv[0].lower()
    ip = argv[1]
    port = int(argv[2])
    id = device + "-" + argv[3]
    
    avg_temp = random.uniform(-30, 50)
    motion_bool = random.choice([0,1])
    feed_start = start
    
    while 1:
        present_time = round(time.time(),5)
        
	if (device == "smart_temperature_sensor"):
            value = str(round(random.normalvariate(avg_temp, 10),1)) + " Degree-Celsius"
            timeout= 1.0
                
            
        elif (device == "smart_motion_detector_camera"):
            
	    if (motion_bool != 0):
         	fps=15
                bitrate= int(random.uniform(50000, 200000)) 
                value = os.urandom(bitrate/8/fps)
                timeout=float(1.0/fps)
                motion_time=float(random.uniform(1,5))
                if((time.time() - feed_start) > motion_time):
                    motion_bool = 0
            else:
                value = "X"
                motion_bool = random.choice([0,1])
                timeout=float(random.uniform(1,10))
                feed_start = time.time() + timeout
    
        else:
            break
        
        message={}    
        message["id"] = str(id)
        message["unix_timestamp"] = str(present_time)
        message["data_size"] = str(len(str(value)))
        message["data"] = str(value)

        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    	server_address = (ip, port)
    	sent = 0
	message_to_send = str(message)    	
	while(sent < len(message_to_send)):
            sent = sent + sock.sendto(message_to_send[sent:len(message_to_send)], server_address)        

        if(device == "smart_temperature_sensor"):
            csv.writer(open(DATA_DIR + id +'.csv', 'ab'), delimiter=',').writerow([present_time, value])
        elif(device == "smart_motion_detector_camera"):
            csv.writer(open(DATA_DIR + id +'.csv', 'ab'), delimiter=',').writerow([present_time, message["data_size"]])
            if(value != "X"):
                feed_data = open(DATA_DIR + id + '.mpeg2', 'ab')
                feed_data.write(str(value))
                feed_data.close
        time.sleep(timeout)

