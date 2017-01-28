class Monster:
	def __init__ (self):
		self.id = None
		self.description = None
		self.hp = None
		self.trophy = None

	#Load Monster Information from the Monster Database
	def load_monster(self,monster_number):
		__filename = "monster_db.txt"
		__monster_match = "Monster Num: " + str(monster_number)
		__switch = False
		self.id = monster_number

		#Open Item Database
		with open(__filename) as fobject:
			rlist = fobject.read().splitlines()

		#Scan Item Database for the correct Item Num
		for data in rlist:
			if data == __monster_match:
				__switch = True

		#Retrieve Item Description
			if __switch:
				if data.startswith('Description:'):
					v,y = data.split(':',1)
					self.description = y.strip()
				elif data.startswith('HP:'):
					v,y = data.split(':',1)
					self.hp = y.strip()
				elif data.startswith('Trophy:'):
					v,y = data.split(':',1)
					self.trophy = y.strip()
				elif not data:
					break
