from helperfunctions import *
class item():
	def __init__(self,identifier,name,description,mass,price):
		self.id = identifier  
		self.name = name
		self.desc = description
		self.mass = mass
		self.price = price
	def use(player):
		return player

class consumable(item):
	def __init__(self,identifier,name,description,mass,price,units):
		self.units = units
		item.__init__(self,identifier,name,description,mass,price)
	def use(self,player):
		output('You consume the '+self.id, player.sobriety)
		if self.units > 0:
			output('You feel slightly more drunk', player.sobriety)
		elif self.units < 0:
			output('You feel slightly sobered up', player.sobriety)

		player.sobriety -= self.units
		player.inventory.remove(self)
		return player


beer_bottle_empty = item('bottle', 'an empty beer bottle','This could be dangerous.',6,0.1)
glass_empty = item('glass','an empty glass','A relic of times gone by.',4.2,0.1)
vodka_bottle_empty = item('vodka bottle', 'an empty vodka bottle', 'description', 6,0.1)
beer_bottle_empty = item('bottle', 'an empty beer bottle','description',6,0.1)
glass_empty = item('glass','an empty glass','description',4.2,0.1)
keys = item('keys','keys','the keys to your flat',0,0.1)
wallet = item('wallet','your wallet','',0,0.1)
phone = item('phone','phone','Your gateway to a Dragon taxi home.',0,0.1)
your_id = item('id','your id','Don\'t lose this.',0,0.1)
drugs = consumable('drugs','drugs','some suspicious white powder',4.2,0,0.1)
hipflask = consumable('hipflask','hipflask','A cheapskates pride and joy.',4.2,0,5)
jacket = item('jacket','your jacket','Keeps you warm, too warm.',4.2,0)
vk = consumable('vk','a bottle of vk','The sweet nectar of the gods.',4.2,1,1)
rum_coke = consumable('rum coke','rum and coke','Suboptimal drink.',4.2,3,2)
gin_tonic = consumable('gin tonic','gin and tonic','Mature student?',4.2,3,2)
vodka_shot = consumable('vodka shot','shot of vodka','Bread and butter of a night out.',4.2,2,2)
jager_bomb = consumable('jagerbomb','Jägerbomb','You don\'t know why you drink these',4.2,2,2)
water = consumable('water','glass of water','a glass of water',4.2,0,-1)
dark_fruits = consumable('dark fruits','can of dark fruits','Reminds you of your year 10 campouts.',4.2,3,2)
red_stripe = consumable('red stripe','can of red stripe','Jamaican you drunk',4.2,3,2)
pint_brains = consumable('brains','pint of brains','You unleash your inner welshman.',4.2,2,2)
bloody_mary = consumable('bloody mary','bloody mary cocktail','A questionable decision.',4.2,4,2)
sourz_shot = consumable('sourz','shot of sourz','A very distinct flavour.',4.2,2,1)
sambuca_shot = consumable('sambuca','shot of sambuca','A shot of sambuca.',4.2,2,2)
whiskey_shot = consumable('whiskey','shot of whiskey','Tastes like scotland.',4.2,3,2)
tequila_shot = consumable('tequila','shot of tequila','Ariba Ariba',4.2,2,2)
wine = consumable('wine','bottle of wine','Only the finest 2017 Lidl Pinot Grigio.',4.2,7,5)
cheeseburger = consumable('cheeseburger','cheeseburger','A wonderous creation.',4.2,1,-1)
chicken_nuggets = consumable('nuggets','chicken nuggets','You hope it\'s chicken.',4.2,4,-2)
mayo_chicken = consumable('mayo chicken','mayo chicken','Chicken slathered in mayo.',4.2,1,-1)
wrap_of_the_day = consumable('wrap','wrap of the day','More like wrap of the night :DDDDDDDDDDDDDDDDDDDDD',4.2,2,-1)
chips = consumable('chips','chips','Greasier than a car engine.',4.2,2,-2)
bigmac = consumable('bigmac','bigmac','The top dog.',4.2,3,-2)
mcflurry = consumable('mcflurry','mcflurry','To cool down after a busy night.',4.2,1,0.1)
kebab = consumable('kebab','kebab','Magical mystery meet.',4.2,3,-2)
a_cheeky_wink = item('wink','a cheeky wink', 'this wink will sure be successful',0,0.1)
irish_disco_biscuit = consumable('irish disco biscuit','irish disco biscuit','I think I know someone who would enjoy this...',4,4,3)
