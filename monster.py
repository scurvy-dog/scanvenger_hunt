
x = []

#Load Monster Information from the Monster Database
def load_monster(monster_number):
	filename = "monster_db.txt"
	monster_number = "Monster: " + str(monster_number)
	switch = False
	#x = []
	
	#Open Monster Database
	with open(filename) as fobject:
		rlist = fobject.read().splitlines()
		
	#Scan Item Database for the correct Monster Num
	for item in rlist:
		if item == monster_number:
			switch = True
	
	#Retrieve Item Description	
		if switch == True:
			if not item:
				switch = False
				break
			
			v,y = item.split(':', 1)
			y = y.strip()
			x.append(y)
	
	#Returning array with Monster Name, Description, HP, and trophy		
	return(x)
				
load_monster(3)	
print x
				