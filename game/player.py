from items import *
from map import rooms
class player_obj():
	def __init__(self):
		self.inventory = [beer_bottle_empty]
		self.hp = 20
		self.sobriety = 10
		self.current_room = rooms["your room"]
		self.money = 30
		self.drugged = False
# Start game at the reception


