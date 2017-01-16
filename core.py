from sys import exit
from room import *
from items import *
from puzzles import *
from monsters import *
from adv_function import *

#DEFINITIONS
player_inventory = []
master_list = ["leash", "bag of kibble", "bone", "squeeky toy"]
game_solve = False
room_num = 0

#START OF GAME:
print "Morgan and Athena's belongings were stolen by a horde of marauding goblins."
print "They need help finding their belongings."
print "Will you help?"

answer = raw_input(">")
answer = answer.lower()
print answer

if answer == "no" or answer == "n":
	print "A comet falls from the sky, reducing you into your component ions. \n"
	#exit(0)

elif answer == "yes" or answer == "y":
	print """
	Great!  Let's begin!
	Athena gives you a bag.  It is currently empty.
	At any time, you can type 'check bag' to ...well, check the bag's contents.

	You ask Morgan and Athena for a list of their belongings.
	Athena looks at you funny, and Morgan smiles and barks.  At any time,
	you can type 'check belongings' to ask Morgan or Athena if you have
	all their belongings.

	To move, type 'go right' or 'go left' or 'go back'.  To begin combat type 'fight'.

	Finally, you can always type 'pick up' to pick up something
	and place it in the bag you were just given.

	Now let's get started!
	"""

else:
	print "In your indecision, you remain rooted to the spot.... For a billion years."
	#exit(0)

#START OF MAIN MODULE
# Set looping condition to run until the game is solved
while game_solve != True:
	# Load The Current Room
	room_values = load_room(room_num)
	# Load any needed items
	if room_values[2] != 0:
		item = load_item(room_values[2])
	# Load any needed monsters
	if room_values[3] != 0:
		monster = load_monster(room_values[3])
	# Load any needed puzzles
	if room_values[4] != 0:
		puzzle = load_puzzle(room_values[4])
	# Extract room exits
	rm_exits = room_values[5]

	# Print room description
	print room_values[1]
	print "\n"

	# Get user input
	command = cli_parser()

	game_solve = True
