from items import *
class npc():
	def __init__(self,name,inventory):
		self.name = name
		self.inventory = inventory

npc_john = npc('John',[beer_bottle_empty])

