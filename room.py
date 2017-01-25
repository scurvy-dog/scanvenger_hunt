class Room:
	def __init__ (self):
		self.id = None
		self.description = None
		self.item = None
		self.monster = None
		self.puzzle = None
		self.exits = None

	def loadroom(self,rm_number):
		__filename = "room_db.txt"
		__room_match = "Room: " + str(rm_number)
		__switch = False
		self.id = rm_number
		x = []

		# Open room file
		with open(__filename) as fobject:
			rlist = fobject.read().splitlines()

		for data in rlist:
	  		if data == __room_match:
				__switch = True
			if __switch:
				if data.startswith('Description:'):
					v,y = data.split(':',1)
					self.description = y.strip()
				elif data.startswith('Item:'):
					v,y = data.split(':',1)
					self.item = y.strip()
				elif data.startswith('Monster:'):
					v,y = data.split(':',1)
					self.monster = y.strip()
				elif data.startswith('Puzzle:'):
					v,y = data.split(':',1)
					self.puzzle = y.strip()
				elif data.startswith('Move:'):
					v,y = data.split(':',1)
					self.exits = y.strip()
				elif not data:
					break
