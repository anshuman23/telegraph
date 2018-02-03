import random
import time

Lights=0
motion_bool = random.choice([0,1]) #Will Be using Anshuman's Code Variable to Detect Motion

Auto=random.choice([0,1])

Availability_of_daylight=random.randrange(0,100)
Bluelight_content=random.randrange(0,100)
Daylight_simulation=random.randrange(0,100)
Dynamic_lighting=random.randrange(0,100)
Tunable_white=random.randrange(0,100)
illumination_of_room_surfaces=random.randrange(0,100)

Luminosity=str(0.2*Availability_of_daylight+0.1*Bluelight_content+0.2*Daylight_simulation+0.2*Dynamic_lighting+0.2*Tunable_white+0.1*illumination_of_room_surfaces)

if(Auto==1):
	
	if(motion_bool==0):
		Lights=0
	else:
		Lights=1
		print "Current Brightness Set to "+ Luminosity+"%"
else:
	print "Set Brightness "		
	Luminosity=raw_input()
	print "Current Brightness Set to "+ Luminosity+"%"

	
	
