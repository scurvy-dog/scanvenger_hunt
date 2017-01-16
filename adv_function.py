# Function definition list for Scavenger Hunt

# Import functions
import random

# CLI parser for valid input
def cli_parser():
	# function variables
	return_code = False
	rand_num = random.randint(1,8)
	invalid_response = [
		"Sorry what?  I wasn't paying attention.",
		"Do you really want to do that?  I don't think that's wise.",
		"Morgan barks at you.",
		"Athena barks at you.",
		"Nope.  Not gonna do that.",
		"You know, that's how the end of the world starts...",
		"Dave.  What are you doing, Dave?",
		"Go Seahawks!",
	]

	# array of valid choices
	command_list = ["check bag","fight","check belongings","pick up","go left","go right",
		"go straight","go up","go down","go back"]

	# Loop condition for valid input
	while return_code != True:
		cli_input = raw_input("What do you do? ")
		#normalize to lower case
		cli_input = cli_input.lower()

		#compare to valid list of commands
		if cli_input in command_list:
			return_code = True
			return (cli_input)
		elif cli_input == "?" or cli_input.lower() =="help":
			print "Available commands: "
			print command_list,
		else:
			rand_num = random.randint(1,8)
			print invalid_response[rand_num]
