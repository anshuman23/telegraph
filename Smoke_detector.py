import random
import time

#True for Lock and False for Open
water_sprinkler=False
option=[True,False]
door=random.choice(option)
windows=random.choice(option)

def timer(n):
	windows=False
	door=False
	print "Timer set for "+str(n)+" Minutes."
	print "Please Evacuate!"
	mins = 0
		# Loop until we reach n minutes running
	while mins != n:
		# Sleep for a minute	
		time.sleep(60)
		# Increment the minute total
		mins += 1
	
	water_sprinkler=True


print "This is a trial Simulation of a Smoke Detector"
while 1:
	ppm=random.randint(1,500)
	print ppm
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


