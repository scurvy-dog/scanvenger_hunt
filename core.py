from sys import exit
from room import *
from item import *
from puzzle import *
from monster import *
from adv_function import *

#DEFINITIONS
player_inventory = []
master_list = ["leash", "bag of kibble", "bone", "squeeky toy"]
game_solve = False
room_num = 0
location = Room()
room_id = 1

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
	location.loadroom(room_id)

	# Load any needed items
	if not location.item:
		item = load_item(location.item)
	# Load any needed monsters
	if not location.monster:
		#monster = load_monster(location.monster)
		pass
	# Load any needed puzzles
	if not location.puzzle:
		puzzle = load_puzzle(location.puzzle)
		pass
	# Extract room exits
	rm_exits = location.exits

	# Print room description

	# Get user input
	command = cli_parser()

	game_solve = True
