from items import *
from helperfunctions import *

class npc():
	def __init__(self,name,inventory,money,hp):
		self.name = name
		self.inventory = inventory
		self.money = money
		self.hp = hp
		self.lines_to = ['Greetings ','background','latest rumours','little advice','little secret','my trade','services','someone in particular','specific places']#need adding
		self.lines_from =['Hi I\'m '+ self.name,'I\'m a student at the university','I heard the Chuckle brothers are around town somewhere','Excessive drinking is bad for your liver','I\'ve heard Kirill will do anything for an irish disco biscuit','I\'m a student','There\'s a guy selling burgers by the student union','I wouldn\'t buy anything off Dave','There\'s a game on tonight so I\'d avoid any Welsh pubs']#need adding
	def talk(self,player):
		item_index = navigate_chat_options(self.lines_to,0)
		output(self.lines_from[item_index],player.sobriety)
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
#class student(npc):

class chuckle_npc(npc):
	def __init__(self,name,inventory,money,hp):
		npc.__init__(self,name,inventory,money,hp)
<<<<<<< HEAD
	def talk(self,player):
		output('To me, to you')
		anykey()
		return player

class kirill_npc(npc):
	def __init__(self,name,inventory,money,hp):
		npc.__init__(self,name,inventory,money,hp)
		self.lines = ['To me','asdsad','asdsad','asdsad','asdsad','asdsad']
	def talk(self,player):
		output('As you begin to apporach Kirill, you realise you need to hand in your game tomorrow and it is nowhere near finished! You wonder if Kirill takes bribes...',player.sobriety)
		if irish_disco_biscuit in player.inventory:
			self.inventory.append(irish_disco_biscuit)
			output('Kirill would you care for an irish disco biscuit?',player.sobriety)
			anykey()

			output('Kirill accepts the drink gratefully.',player.sobriety)


		anykey()
		return player

npc_john = npc('John',[beer_bottle_empty,phone],4.50,5.0)
npc_jill = npc('Jill', [vk], 5.0, 5.0)
npc_kirill =kirill_npc('Kirill', [vodka_bottle_empty], 100.0, 1000.0)
npc_Chuckle_1 = chuckle_npc('Barry Chuckle',[drugs], 0.0, 10.0)
npc_Chuckle_2 = chuckle_npc('Paul Chuckle', [drugs], 0.0, 10.0)
npc_gaz = npc('Gaz', [], 4.0, 6.0)
npc_homeless = npc('Homeless man', [beer_bottle_empty], 0.0, 1.0)
npc_mcdonalds = shop_npc("Worker", [cheeseburger,beefburger, chicken_nuggets, mayo_chicken, wrap_of_the_day, chips, mcflurry], 100.0, 30.0)
npc_burger = shop_npc("Burgerman", [cheeseburger,beefburger], 20.0, 40.0)
npc_welsh_bar = shop_npc('Bartender', [pint_brains], 50.0,10.0)
npc_welsh_man = npc('Dafydd ap Evans',[pint_brains],20,10)
npc_su_bar = shop_npc('Bartender', [vk,rum_coke, gin_tonic, vodka_shot, jager_bomb, water, dark_fruits, red_stripe, bloody_mary, sourz_shot, irish_disco_biscuit, sambuca_shot, whiskey_shot, tequila_shot, wine, irish_disco_biscuit], 100.0,5.0)
npc_pryzm_bar= shop_npc('Bartender', [vk,rum_coke, gin_tonic, vodka_shot, jager_bomb, water, dark_fruits, red_stripe, bloody_mary, sourz_shot, sambuca_shot, whiskey_shot, tequila_shot, wine, irish_disco_biscuit], 200.0,5.0)
npc_tiger_tiger_bar = shop_npc('Bartender', [vk,rum_coke, gin_tonic, vodka_shot, jager_bomb, water, dark_fruits, red_stripe, bloody_mary, sourz_shot, sambuca_shot, whiskey_shot, tequila_shot, wine], 100.0,5.0)
npc_welsh_man2 = npc('Gruffydd ap ?',[pint_brains],20,10)
npc_dealer = shop_npc('Dodgy Dan',[drugs],8,10)
npc_bouncer = npc('Bouncer',[powerful_fist],4,20)
#rum_coke gin_tonic vodka_shot jager_bomb water dark_fruits red_stripe pint_brains bloody_mary sourz_shot sambuca_shot whiskey_shot tequila_shot wine