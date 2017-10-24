from items import *
class npc():
	def __init__(self,name,inventory,money,hp, lines = ['Hello','buy']):
		self.name = name
		self.inventory = inventory
		self.money = money
		self.hp = hp
		self.lines = lines




npc_john = npc('John',[beer_bottle_empty,phone],4.50,5.0,['Hello','Buy'])
npc_jill = npc('Jill', [vk], 5.0, 5.0)
npc_kirill =npc('Kirill', [vodka_bottle_empty], 100.0, 1000.0)
npc_Chuckle_1 = npc('Barry Chuckle',[drugs], 0.0, 10.0)
npc_Chuckle_2 = npc('Paul Chuckle', [drugs], 0.0, 10.0)
npc_gaz = npc('Gaz', [], 4.0, 6.0)
npc_homeless = npc('Homeless man', [beer_bottle_empty], 0.0, 1.0)

