#Smart_Fridge
'''
Fridge is Divided into Different Zones
1. The door:Warmest part of the fridge and subject to the most temperature fluctuations, so avoid storing highly perishable foods on the door
2. Upper shelves:Usually constant in temperature. Use them for dairy products, drinks, containers of leftovers
3. Bottom shelf:This is often the coldest spot in the fridge. It's a good place to store meat, fish, and eggs
4. Crisper drawers:Drawers do tend to retain some moisture, though, which is good for produce
'''


Temperature_of_Zones={'1':8,'2':5,'3':4,'4':6}

def Water_Dispenser(Quantity):
	print "Please Position your Bottle"
	print "Filling "+Quantity+" Litres"

def Find_Zone(Find):
	Zone={'Fruits':'Shelf'} #Will Add More Items Later

	if(Zone.has_key(Find)==True):
		print "Commodity Should be placed in "+Zone[Find]
	else:
		print "Commodity Not Available in General List of Items!"

def Adjust_Temperature(Zone,Temp):
	Temperature_of_Zones[Zone]=Temp
	print "Temperature adjusted to "+Temp+" degree celsius for Zone "+Zone	


while 1:
	print "\n"
	print "Select Among the Options:"
	print "1. Water Dispenser"
	print "2. Smart Zone Finder"
	print "3. Adjust Temperature"
	print "4. Exit"
	

	choice=input()
#print choice
	
	if (choice==1):
		Quantity=raw_input("Enter Quantity in litres:")
		Water_Dispenser(Quantity)

	elif (choice==2):
		Find=raw_input("Enter the Commodity for which you want to find the Appropriate Zone in the Refrigerator:")
		Find_Zone(Find)	

	elif(choice==3):
		Zone=raw_input("Enter Zone(1/2/3/4):")
		Temp=raw_input("Enter Temperature(Degree celsius):")
		Adjust_Temperature(Zone,Temp)
	else:
		break

