
x = []

#Load Item Information from the Item Database
def load_item(item_number):
	filename = "item_db.txt"
	item_number = "Item Num: " + str(item_number)
	switch = False
	#x = []
	
	#Open Item Database
	with open(filename) as fobject:
		rlist = fobject.read().splitlines()
		
	#Scan Item Database for the correct Item Num
	for item in rlist:
		if item == item_number:
			switch = True
	
	#Retrieve Item Description	
		if switch == True:
			if not item:
				switch = False
				break
			
			v,y = item.split(':', 1)
			y = y.strip()
			x.append(y)
	
	#Returning array with Item Description
	return(x)				
	
load_item(1)
print x	