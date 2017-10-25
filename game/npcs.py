from items import *
from helperfunctions import *
class npc():
	def __init__(self,name,inventory,money,hp):
		self.name = name
		self.inventory = inventory
		self.money = money
		self.hp = hp
		self.lines = ['Hello '+ self.name,'']
	def talk(self,player):
		item_index = navigate_chat_options(self.lines,0)
		output(['Hello','basdsad','aasdsad','sasdsad','fasdsad','hasdsad'][item_index],player.sobriety)
		anykey()
		return player
		
class shop_npc(npc):
	def __init__(self,name,inventory,money,hp):
		npc.__init__(self,name,inventory,money,hp)
	def talk(self,player):
		item_index = navigate_chat_options([item.name + '     £' + str(item.price) for item in self.inventory],0)
		if player.money >= self.inventory[item_index].price:
			player.money -= self.inventory[item_index].price
			player.inventory.append(self.inventory[item_index])
		else:
			print('That is too expensive')
			anykey()
		return player

class chuckle_npc(npc):
	def __init__(self,name,inventory,money,hp):
		npc.__init__(self,name,inventory,money,hp)
		self.lines = ['To me','asdsad','asdsad','asdsad','asdsad','asdsad']
	def talk(self,player):
		item_index = navigate_chat_options(self.lines,0)
		output(['To you','basdsad','aasdsad','sasdsad','fasdsad','hasdsad'][item_index],player.sobriety)
		anykey()
		return player

npc_john = npc('John',[beer_bottle_empty,phone],4.50,5.0)
npc_jill = npc('Jill', [vk], 5.0, 5.0)
npc_kirill =npc('Kirill', [vodka_bottle_empty], 100.0, 1000.0)
npc_Chuckle_1 = chuckle_npc('Barry Chuckle',[drugs], 0.0, 10.0)
npc_Chuckle_2 = chuckle_npc('Paul Chuckle', [drugs], 0.0, 10.0)
npc_gaz = npc('Gaz', [], 4.0, 6.0)
npc_homeless = npc('Homeless man', [beer_bottle_empty], 0.0, 1.0)
npc_su_bar = shop_npc('Bartender', [vk,vk,vk,vk,vk,vk,vk,vk], 100.0,5.0)
npc_pryzm_bar= shop_npc('Bartender', [rum_coke, rum_coke, rum_coke, gin_tonic, gin_tonic, gin_tonic, sambuca_shot, sambuca_shot, whiskey_shot, whiskey_shot, tequila_shot, tequila_shot], 200.0,5.0)
npc_tiger_tiger_bar = shop_npc('Bartender', [tequila_shot,tequila_shot, rum_coke, rum_coke, rum_coke, gin_tonic, gin_tonic, gin_tonic, sambuca_shot, sambuca_shot, whiskey_shot, whiskey_shot], 100.0,5.0)
npc_welsh_bar = shop_npc('Bartender', [pint_brains, pint_brains], 50.0,10.0)
npc_welsh_man = npc('Dafydd ap Evans',[pint_brains, pint_brains],20,10)
npc_su_bar = shop_npc('Bartender', [vk,rum_coke, gin_tonic, vodka_shot, jager_bomb, water, dark_fruits, red_stripe, bloody_mary, sourz_shot, sambuca_shot, whiskey_shot, tequila_shot, wine], 100.0,5.0)
npc_pryzm_bar= shop_npc('Bartender', [vk,rum_coke, gin_tonic, vodka_shot, jager_bomb, water, dark_fruits, red_stripe, bloody_mary, sourz_shot, sambuca_shot, whiskey_shot, tequila_shot, wine], 200.0,5.0)
npc_tiger_tiger_bar = shop_npc('Bartender', [vk,rum_coke, gin_tonic, vodka_shot, jager_bomb, water, dark_fruits, red_stripe, bloody_mary, sourz_shot, sambuca_shot, whiskey_shot, tequila_shot, wine], 100.0,5.0)
npc_welsh_bar = shop_npc('Bartender', [pint_brains], 50.0,10.0)
npc_welsh_man = npc('Dafydd ap Evans',[pint_brains],20,10)


#rum_coke gin_tonic vodka_shot jager_bomb water dark_fruits red_stripe pint_brains bloody_mary sourz_shot sambuca_shot whiskey_shot tequila_shot wine