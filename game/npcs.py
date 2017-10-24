from items import *
class npc():
	def __init__(self,name,inventory,money,hp):
		self.name = name
		self.inventory = inventory
		self.money = money
		self.hp = hp

npc_john = npc('John',[beer_bottle_empty],4.50,5.0)

