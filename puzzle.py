class Puzzle:
	def __init__ (self):
		self.id = None
		self.name = None
		self.trophy = None

	#Load puzzle Information from the puzzle Database
	def load_puzzle(self,puzzle_number):
		__filename = "puzzle_db.txt"
		__puzzle_match = "Puzzle Num: " + str(puzzle_number)
		__switch = False
		self.id = puzzle_number

		#Open Item Database
		with open(__filename) as fobject:
			rlist = fobject.read().splitlines()

		#Scan Item Database for the correct Item Num
		for data in rlist:
			if data == __puzzle_match:
				__switch = True

		#Retrieve Item Description
			if __switch:
				if data.startswith('Name:'):
					v,y = data.split(':',1)
					self.name = y.strip()
				elif data.startswith('Trophy:'):
					v,y = data.split(':',1)
					self.trophy = y.strip()
				elif not data:
					break
