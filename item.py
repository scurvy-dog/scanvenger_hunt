
#Load Item Information from the Item Database
class Item:
	def __init__ (self):
		self.id = None
		self.description = None

	def load_item(self,item_number):
		__filename = "item_db.txt"
		__item_match = "Item Num: " + str(item_number)
		__switch = False
		self.id = item_number
		#Open Item Database
		with open(__filename) as fobject:
			rlist = fobject.read().splitlines()

		#Scan Item Database for the correct Item Num
		for data in rlist:
			if data == __item_match:
				__switch = True

		#Retrieve Item Description
			if __switch:
				if data.startswith('Description:'):
					v,y = data.split(':',1)
					self.description = y.strip()
				elif not data:
					break
