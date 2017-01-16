# Puzzle Definitions for Scavenger Hunt

# Define Variables

def load_puzzle(puzzle_number):
	filename = "puzzle_db.txt"
	puzzle_number = "Puzzle: " + str(puzzle_number)
	switch = False
	x = []

	# Open room file
	with open(filename) as fobject:
		rlist = fobject.read().splitlines()

	for item in rlist:
  		if item == puzzle_number:
			# True when we find the correct room number
			switch = True
  		if switch:
			if not item:
				# Blank line will be end of room information
				switch = False
				# Stop reading items from rlist and return function
				break
 			# remove field description into v and value to y
			v,y = item.split(':',1)
			# remove leading or trailing white space
			y=y.strip()
			# Append values to list
			x.append(y)
			# Blank line will be end of room information
	return(x)
